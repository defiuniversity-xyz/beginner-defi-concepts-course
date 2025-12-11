#!/usr/bin/env python3
"""
Upload audio and video media files to Google Cloud Storage for Beginner DeFi Concepts GitBook.
Organizes files by lesson: lesson-{NN}/audio/ and lesson-{NN}/video/
"""

from google.cloud import storage
import os
import mimetypes
import re
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
GITBOOK_DIR = SCRIPT_DIR.parent
ROOT_DIR = GITBOOK_DIR.parent.parent  # Go up from basic-defi-crypto-concepts-ebook to ebooks to root
DEFAULT_SERVICE_ACCOUNT = ROOT_DIR / 'Keys' / 'google-service-account.json'

SERVICE_ACCOUNT_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', str(DEFAULT_SERVICE_ACCOUNT))
BUCKET_NAME = os.getenv('GCS_BUCKET_NAME', 'beginner-defi-crypto-concepts-gitbook-media')
PROJECT_ID = 'defi-university'

def extract_lesson_number(filename):
    """Extract lesson number from filename (e.g., 'lesson1' -> 1, 'lesson10' -> 10)"""
    match = re.search(r'lesson(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def format_lesson_slug(lesson_num):
    """Format lesson number as slug (e.g., 1 -> 'lesson-01', 10 -> 'lesson-10')"""
    return f"lesson-{lesson_num:02d}"

def upload_media_files():
    """Upload all audio and video files to Google Cloud Storage"""
    
    # Verify service account file exists
    service_account_abs = os.path.abspath(SERVICE_ACCOUNT_PATH)
    if not os.path.exists(service_account_abs):
        # Try alternative paths
        alt_paths = [
            str(DEFAULT_SERVICE_ACCOUNT),
            str(ROOT_DIR / 'Keys' / 'google-service-account.json'),
            os.path.expanduser('~/Keys/google-service-account.json'),
        ]
        found = False
        for alt_path in alt_paths:
            if os.path.exists(alt_path):
                service_account_abs = os.path.abspath(alt_path)
                found = True
                break
        
        if not found:
            print(f"ERROR: Service account file not found: {SERVICE_ACCOUNT_PATH}")
            print("Tried alternative paths:", alt_paths)
            print("Please set GOOGLE_APPLICATION_CREDENTIALS environment variable")
            return False
    
    # Set environment variable for Google Cloud authentication
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_abs
    
    # Setup Google Cloud Storage client
    try:
        storage_client = storage.Client(project=PROJECT_ID)
        bucket = storage_client.bucket(BUCKET_NAME)
        # Try to check if bucket exists, but continue even if check fails (may not have bucket.get permission)
        try:
            if not bucket.exists():
                print(f"Bucket '{BUCKET_NAME}' does not exist.")
                print(f"Please create it manually using:")
                print(f"  gcloud storage buckets create gs://{BUCKET_NAME} --project={PROJECT_ID} --location=US --uniform-bucket-level-access")
                print(f"  gcloud storage buckets add-iam-policy-binding gs://{BUCKET_NAME} --member=allUsers --role=roles/storage.objectViewer --project={PROJECT_ID}")
                return False
            print(f"✓ Using existing bucket: {BUCKET_NAME}")
        except Exception as check_error:
            # If we can't check existence, assume bucket exists and try to upload
            # This handles cases where service account has object permissions but not bucket.get
            print(f"⚠️  Could not verify bucket existence (may not have bucket.get permission)")
            print(f"   Proceeding with upload to: {BUCKET_NAME}")
    except Exception as e:
        print(f"ERROR: Failed to connect to Google Cloud Storage: {e}")
        return False
    
    # Find all audio and video files
    gitbook_dir = SCRIPT_DIR.parent
    audio_dir = gitbook_dir / 'content' / 'audio'
    video_dir = gitbook_dir / 'content' / 'video'
    
    if not audio_dir.exists():
        print(f"ERROR: Audio directory not found: {audio_dir}")
        return False
    
    if not video_dir.exists():
        print(f"ERROR: Video directory not found: {video_dir}")
        return False
    
    # Find all media files
    audio_files = sorted(audio_dir.glob("*.m4a"))
    video_files = sorted(video_dir.glob("*.mp4"))
    
    if not audio_files and not video_files:
        print(f"No media files found in {audio_dir} or {video_dir}")
        return False
    
    print(f"Found {len(audio_files)} audio files and {len(video_files)} video files")
    print(f"Uploading to: gs://{BUCKET_NAME}/")
    print("=" * 60)
    
    uploaded = []
    failed = []
    embed_syntax = {}
    
    # Upload audio files
    print("\n📢 Uploading Audio Files...")
    print("-" * 60)
    for audio_file in audio_files:
        lesson_num = extract_lesson_number(audio_file.name)
        if not lesson_num:
            print(f"⚠️  Could not extract lesson number from: {audio_file.name}")
            failed.append((audio_file.name, "audio", "Could not extract lesson number"))
            continue
        
        lesson_slug = format_lesson_slug(lesson_num)
        object_key = f"{lesson_slug}/audio/{audio_file.name}"
        
        try:
            print(f"Uploading: {audio_file.name} → {object_key}")
            
            blob = bucket.blob(object_key)
            blob.content_type = 'audio/mp4'  # MIME type for .m4a files
            blob.upload_from_filename(str(audio_file))
            
            url = f"https://storage.googleapis.com/{BUCKET_NAME}/{object_key}"
            uploaded.append((audio_file.name, object_key, "audio"))
            embed_syntax[lesson_num] = embed_syntax.get(lesson_num, {})
            embed_syntax[lesson_num]['audio'] = url
            print(f"  ✓ Success: {url}")
            
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            failed.append((audio_file.name, "audio", str(e)))
    
    # Upload video files
    print("\n🎬 Uploading Video Files...")
    print("-" * 60)
    for video_file in video_files:
        lesson_num = extract_lesson_number(video_file.name)
        if not lesson_num:
            print(f"⚠️  Could not extract lesson number from: {video_file.name}")
            failed.append((video_file.name, "video", "Could not extract lesson number"))
            continue
        
        lesson_slug = format_lesson_slug(lesson_num)
        object_key = f"{lesson_slug}/video/{video_file.name}"
        
        try:
            print(f"Uploading: {video_file.name} → {object_key}")
            
            blob = bucket.blob(object_key)
            blob.content_type = 'video/mp4'
            blob.upload_from_filename(str(video_file))
            
            url = f"https://storage.googleapis.com/{BUCKET_NAME}/{object_key}"
            uploaded.append((video_file.name, object_key, "video"))
            embed_syntax[lesson_num] = embed_syntax.get(lesson_num, {})
            embed_syntax[lesson_num]['video'] = url
            print(f"  ✓ Success: {url}")
            
        except Exception as e:
            print(f"  ✗ Failed: {e}")
            failed.append((video_file.name, "video", str(e)))
    
    # Print summary
    print("\n" + "=" * 60)
    print(f"Upload Summary:")
    print(f"  ✅ Successfully uploaded: {len(uploaded)} files")
    print(f"  ❌ Failed: {len(failed)} files")
    
    if failed:
        print(f"\nFailed files:")
        for filename, media_type, error in failed:
            print(f"  - {media_type}: {filename} ({error})")
    
    # Print GitBook embed syntax
    if embed_syntax:
        print("\n" + "=" * 60)
        print("GitBook Embed Syntax (copy to lesson files):")
        print("=" * 60)
        for lesson_num in sorted(embed_syntax.keys()):
            lesson_data = embed_syntax[lesson_num]
            print(f"\n--- Lesson {lesson_num} ---")
            if 'audio' in lesson_data:
                print('{% embed url="' + lesson_data["audio"] + '" %}')
            if 'video' in lesson_data:
                print('{% embed url="' + lesson_data["video"] + '" %}')
    
    print("\n" + "=" * 60)
    
    return len(failed) == 0

if __name__ == "__main__":
    success = upload_media_files()
    exit(0 if success else 1)

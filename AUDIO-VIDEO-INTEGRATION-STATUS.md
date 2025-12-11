# Audio and Video Integration Status

**Date:** December 10, 2025

## Completed

### 1. Upload Script Created
- **File:** `tools/upload_media_to_gcs.py`
- **Purpose:** Uploads all 12 audio (.m4a) and 12 video (.mp4) files to Google Cloud Storage
- **Bucket:** `beginner-defi-crypto-concepts-gitbook-media`
- **Structure:** `lesson-{NN}/audio/` and `lesson-{NN}/video/`

### 2. All 12 Lessons Updated
All lesson files now have audio and video embeds at the top (immediately after YAML frontmatter):

- ✅ lesson-01-the-evolution-of-money-and-trust.md
- ✅ lesson-02-tradfi-cefi-and-defi.md
- ✅ lesson-03-blockchain-infrastructure.md
- ✅ lesson-04-smart-contracts-and-token-standards.md
- ✅ lesson-05-wallets-and-self-custody.md
- ✅ lesson-06-security-fundamentals.md
- ✅ lesson-07-decentralized-exchanges.md
- ✅ lesson-08-defi-lending-and-borrowing.md
- ✅ lesson-09-stablecoins-and-stability-mechanisms.md
- ✅ lesson-10-flash-loans-and-advanced-primitives.md
- ✅ lesson-11-risk-management.md
- ✅ lesson-12-layer-2s-and-the-future-of-defi.md

**Embed Format:**
```markdown
{% embed url="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-{NN}/audio/{filename}" %}

{% embed url="https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-{NN}/video/{filename}" %}
```

## Next Steps Required

### 1. Create Google Cloud Storage Bucket

Run these commands to create the bucket and set public access:

```bash
gcloud storage buckets create gs://beginner-defi-crypto-concepts-gitbook-media \
  --project=defi-university \
  --location=US \
  --uniform-bucket-level-access

gcloud storage buckets add-iam-policy-binding gs://beginner-defi-crypto-concepts-gitbook-media \
  --member=allUsers \
  --role=roles/storage.objectViewer \
  --project=defi-university
```

**Note:** Requires `gcloud auth login` if not already authenticated.

### 2. Upload All Media Files

Once the bucket is created, run the upload script:

```bash
cd "/Users/m00nsh0t/Documents/Testimonials Insert/ebooks/basic-defi-crypto-concepts-ebook/tools"
python3 upload_media_to_gcs.py
```

This will upload:
- 12 audio files (.m4a) → `lesson-{NN}/audio/`
- 12 video files (.mp4) → `lesson-{NN}/video/`

### 3. Verify Uploads

After uploading, verify files are accessible:

```bash
# Test a sample URL
curl -I "https://storage.googleapis.com/beginner-defi-crypto-concepts-gitbook-media/lesson-01/audio/lesson1 History_of_Blockchain_Before_Bitcoin.m4a"
```

Should return `HTTP/2 200` if successful.

## File Mapping

### Audio Files (12 files)
1. `lesson1 History_of_Blockchain_Before_Bitcoin.m4a` → `lesson-01/audio/`
2. `lesson2 TradFi_CeFi_DeFi_Architecture_and_Risk.m4a` → `lesson-02/audio/`
3. `lesson3 Blockchain_Trilemma_and_Layer_2_Rollups.m4a` → `lesson-03/audio/`
4. `lesson4 Automated_Trust_Built_With_Money_Legos.m4a` → `lesson-04/audio/`
5. `lesson5 Seed_Phrases_Private_Keys_Wallet_Security.m4a` → `lesson-05/audio/`
6. `lesson6 Token_Approvals_Are_Your_DeFi_Security_Debt.m4a` → `lesson-06/audio/`
7. `lesson7 AMM_Math_and_Impermanent_Loss_Explained.m4a` → `lesson-07/audio/`
8. `lesson8 DeFi_Lending_Overcollateralization_and_Liquidation_Math.m4a` → `lesson-08/audio/`
9. `lesson9 Stablecoin_Trilemma_and_Its_Three_Types.m4a` → `lesson-09/audio/`
10. `lesson10 Flash_Loans_Weaponizing_Instant_Capital.m4a` → `lesson-10/audio/`
11. `lesson11 DeFi_Risk_Framework_Five_Mitigation_Steps.m4a` → `lesson-11/audio/`
12. `lesson12 Rollups_Real_World_Assets_Institutional_DeFi.m4a` → `lesson-12/audio/`

### Video Files (12 files)
1. `lesson1 The_History_of_Trust.mp4` → `lesson-01/video/`
2. `lesson2 TradFi,_CeFi,_&_DeFi.mp4` → `lesson-02/video/`
3. `lesson3 The_Blockchain_Trilemma.mp4` → `lesson-03/video/`
4. `lesson4 Vending_Machines_to_Money_Legos.mp4` → `lesson-04/video/`
5. `lesson5 Crypto_Self-Custody.mp4` → `lesson-05/video/`
6. `lesson6 Crypto_s_Approval_Threat.mp4` → `lesson-06/video/`
7. `lesson7 Engine_of_DeFi_Trading.mp4` → `lesson-07/video/`
8. `lesson8 DeFi_Lending_Demystified.mp4` → `lesson-08/video/`
9. `lesson9 Stablecoins__Digital_Dollar.mp4` → `lesson-09/video/`
10. `lesson10 Flash_Loans__DeFi_s_Magic.mp4` → `lesson-10/video/`
11. `lesson11 Navigating_DeFi_Risk.mp4` → `lesson-11/video/`
12. `lesson12 The_Future_of_DeFi.mp4` → `lesson-12/video/`

## Expected Result

After uploading files to GCS:
- GitBook will automatically render audio embeds as clickable audio players
- GitBook will automatically render video embeds as embedded video players
- Audio and video will appear at the top of each lesson
- All media will be accessible via public URLs

## Service Account

The upload script uses the service account at:
- `Keys/google-service-account.json` (relative to project root)
- Or set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

The service account must have:
- `storage.objects.create` permission
- `storage.objects.get` permission
- (Optional) `storage.buckets.create` if bucket doesn't exist

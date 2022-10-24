# Google Wallet Passes
Sources and instructions to generate Google Wallet passes with a UID and barcode on them. It requires Google issuer and cloud platform accounts.

## Instructions
1. Obtain a service key JSON file, either by getting it from someone who already downloaded it, or by making a new one [here](https://console.cloud.google.com/iam-admin/serviceaccounts/) (in Google Cloud console under IAM & Admin > Service Accounts). See [here](https://developers.google.com/wallet/retail/loyalty-cards/web/prerequisites) for how to generate a new key.
1. Verify that the `issuer_id` and `class_id` variables in the `makepasslink()` function in `genpasslink.py` are set correctly and match the desired class type in the Google Pay & Wallet [console](https://pay.google.com/business/console/) (under Google Wallet API).
1. Generate a single pass with an invocation like this (quotes are required around the name)

        ./genpasslink.py service_key_file.json "Mr. Student" 115333333 21430018888888
     
   Or generate multiple passes from an Excel document with 

        ./genpasslink.py service_key_file.json ../students.xlsx

1. This will generate a very long URL for each pass generated. Send this URL to the desired recipient. When generating multiple passes, it will first print out the names of the individuals whose passes are being generated, followed by the pass URLs in the same order.

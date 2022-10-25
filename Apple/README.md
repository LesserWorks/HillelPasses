# Apple Wallet Passes
Sources and instructions to generate Apple Wallet passes with a UID and barcode on them. You must be on a Mac to generate passes and have Xcode installed.

## Instructions
1. Follow the instructions [here](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/YourFirst.html) for how to download the requisite Pass Type ID certificate from the Apple Developer portal.
1. Double click on the downloaded certificate to add it to Keychain Access.
1. Double click on the certificate within Keychain Access and note what it says for the "Organizational Unit" within the "Issuer Name" section. For example, it may say "G4".
1. Download the corresponding Worldwide Developer Relations intermediate certificate from [this page](https://www.apple.com/certificateauthority/) and once again add it to Keychain Access.
1. Download and compile (with Xcode) the [signpass tool](https://developer.apple.com/services-account/download?path=/iOS/Wallet_Support_Materials/WalletCompanionFiles.zip) (can also be found on the first page linked above). It makes the signing process much easier.
1. The compiled executable will be in `/Users/yourname/Library/Developer/Xcode/DerivedData/signpass-blahblah/Build/Products/Debug`. Move the executable to `HillelPasses/Apple`.
1. Verify that the `passTypeIdentifier` and `teamIdentifier` fields in `pass.json` are correct and match the values in the Apple Developer portal.
1. Generate a single pass with an invocation like this (quotes are required around the name)

        ./genpass.py HillelMealCard.pass/ "Mr. Student" 115333333 21430018888888
     
   Or generate multiple passes from an Excel document with 

        ./genpass.py HillelMealCard.pass/ ../students.xlsx DestinationDir/

1. Each resulting pass file will end in `*.pkpass`. You can email or WhatsApp the file directly, and you can also drag the pass file into an iPhone simulator to make sure it was made correctly.

### Distributing Passes via Links
If you generated a whole folder full of passes, follow these instructions to generate a download link for each one:
1. Upload the whole folder to Google Drive (using the "Folder Upload" button)
1. Set the sharing permissions on the Google Drive folder to "Anyone with the link can view"
1. Get the URL of the Google Drive folder (**WITHOUT** anything at the end, like `/edit?usp=sharing`)
1. Get your Google Drive API key from [Google Cloud console](https://console.cloud.google.com/apis/credentials) (under APIs and Services > Credentials)
1. Invoke the `getFileURL.py` script as follows

        ./getFileURLs.py --key=<api key> --folder-url=<google drive folder url>

1. This will first print out all the file names alphabetically, and then print out a corresponding download link for each one, in the same order as the names above.

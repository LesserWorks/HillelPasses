# Apple Wallet Passes
Sources and instructions to generate Apple wallet passes with a UID barcode on them. You must be on a Mac to generate passes and have Xcode installed.

## Instructions
1. Follow the instructions [here](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/YourFirst.html) for how to download the requisite Pass Type ID certificate from the Apple Developer portal.
1. Double click on the downloaded certificate to add it to Keychain Access.
1. Double click on the certificate within Keychain Access and note what it says for the "Organizational Unit" within the "Issuer Name" section. For example, it may say "G4".
1. Download the corresponding Worldwide Developer Relations intermediate certificate from [this page](https://www.apple.com/certificateauthority/) and once again add it to Keychain Access.
1. Download and compile (with Xcode) the signpass tool from [here](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/YourFirst.html). It makes the signing process much easier. The executable will be in `/Users/yourname/Library/Developer/Xcode/DerivedData/signpass-blahblah/Build/Products/Debug`
1. Move the signpass executable to `HillelPasses/Apple`
1. Make sure the `genpass.py` file is executable with `sudo chmod +x genpass.py`.
1. Generate a single pass with an invocation like 

        ./genpass.py ./HillelMealCard.pass "Eric Gulich" 115333333 21430018888888
     
   Or generate multiple passes from an Excel document with 
   
        ./genpass.py ./HillelMealCard.pass ./students.xlsx ./DestinationDir/

1. The resulting pass file will end in `*.pkpass`. You can email or WhatsApp the file directly, or you can upload the pass to Google drive and send people this link which will directly download it: `https://drive.google.com/uc?export=download&id=FILE_ID`
You can also drag the pass file into an iPhone simulator to make sure it was made correctly.
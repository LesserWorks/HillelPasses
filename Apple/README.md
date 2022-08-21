# Apple Wallet Passes
Sources and instructions to generate Apple wallet passes with a UID barcode on them.

# Instructions
1. Follow the instructions [here](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/YourFirst.html) for how to download the requisite certificates from the Apple Developer portal.
2. Download and compile (with Xcode) the signpass tool from the same page. It makes the signing process much easier. The executable will be in `/Users/yourname/Library/Developer/Xcode/DerivedData/signpass-blahblah/Build/Products/Debug`
3. Move the signpass executable to `HillelPasses/Apple`
4. Sign the pass with `./signpass -p HillelMealCard.pass`
5. If it signed successfully, email or WhatsApp the resulting `HillelMealCard.pkpass` file. You can also drag it into an iPhone simulator.
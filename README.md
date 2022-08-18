# HillelPasses
Sources and instructions to generate digital passes with a UID barcode on them.

# Instructions
1. Follow the instructions [here](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/YourFirst.html#//apple_ref/doc/uid/TP40012195-CH2-SW1) for how to download the requisite certificates from the Apple Developer portal.
2. If desired also, download and compile (with Xcode) the signpass tool from the same page. It makes the signing process much easier. The executable will be in /Users/<username>/Library/Developer/Xcode/DerivedData/signpass-blahblah/Build/Products/Debug
3. Place the signpass executable in ./HillelPasses
4. Sign the pass with `./signpass -p HillelMealCard.pass`
5. If it signed successfully, email or WhatsApp the HillelMealCard.pkpass file. You can also drag it into an iPhone simulator.
with import <nixpkgs> {};
stdenv.mkDerivation rec {
  name = "env";
  buildInputs = [
    python3
    python3Packages.beautifulsoup4
    python3Packages.dateutil
    python3Packages.jsonpickle
    python3Packages.matplotlib
    python3Packages.requests
    python3Packages.requests-cache
    jupyter
  ];
}

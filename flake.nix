{
  description = "A flake providing a Python environment with numpy and matplotlib on Darwin and Linux systems";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-darwin" ];
      devShellFor = system: let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python311;
      in pkgs.mkShell {
        buildInputs = [
          python
          python.pkgs.numpy
          python.pkgs.matplotlib
        ];
      };
    in {
      devShells = builtins.listToAttrs (map (system: {
        name = system;
        value = {
          default = devShellFor system;
        };
      }) systems);
    };
}
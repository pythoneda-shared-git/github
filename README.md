# Github shared kernel

This package interacts with github via its REST API.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-git/github/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-git-github = {
      [optional follows]
      url =
        "github:pythoneda-shared-git-def/github/[version]";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is managed by the [https://github.com/pythoneda-shared-git-def/github](github "github") definition repository.


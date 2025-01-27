# SFML Simple 2D Game: Scroll of the Undead

![GitHub](https://img.shields.io/github/license/mataktelis11/Simple-SFML-2D-Game)
![GitHub top language](https://img.shields.io/github/languages/top/mataktelis11/Simple-SFML-2D-Game)

This is a free and open-source game based on the source code provided by the book <a href="https://www.packtpub.com/product/sfml-game-development-by-example/9781785287343" target="_blank">SFML Game Development By Example (ISBN 9781785287343)</a>.

<img src="/docs/screenshots/1.png" alt="Alt text" title="In-Development Screenshot">


## Intro
This repository is a fork from <a href="https://github.com/sschellhoff/SFMLGameDevelopmentByExample" target="_blank">sschellhoff</a> who provided the original book's source code in a runnable version.

Here is a video demo

[demo.webm](https://github.com/mataktelis11/Simple-SFML-2D-Game/assets/61196956/775ab4ba-fe83-4103-a83b-408e93744556)

## Build Instructions

### Linux

#### Prerequisites

Install SFML from your package manager. Also, make sure you have ```cmake``` and ```g++```.

For Debian based distros:
```
$ sudo apt install libsfml-dev cmake build-essential
```
For Arch-based distros:
```
$ pacman -Syu cmake sfml base-devel 
```

#### Build

Build from source
```
$ git clone https://github.com/mataktelis11/Simple-SFML-2D-Game.git
$ cd Simple-SFML-2D-Game
$ mkdir build && cd build
$ cmake ..
$ cmake --build .
```
This will generate an executable file called **ScrollOfTheUndead** in the current dir.

### Windows

#### Prerequisites
- <a href="https://cmake.org/" target="_blank">CMake</a>
- <a href="https://git-scm.com/downloads" target="_blank">Git</a>
- <a href="https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/7.3.0/threads-posix/seh/x86_64-7.3.0-release-posix-seh-rt_v5-rev0.7z/download" target="_blank">MinGW 7.3.0 64 bit</a>
- <a href="https://www.sfml-dev.org/files/SFML-2.5.1-windows-gcc-7.3.0-mingw-64-bit.zip" target="_blank">SFML 2.5.1 for MinGW 7.3.0</a>

Make sure that CMake, git, SFML and mingw are in your path. If this is your first time compiling an SFML project on Windows you can check out <a href="https://wfale.net/2023/01/02/sfml-c-and-windows-quick-guide-to-awesome-graphics/" target="_blank">this</a> helpful guide.


#### Build

Open cmd or gitbash and type the following commands to build from source

```
$ git clone https://github.com/mataktelis11/Simple-SFML-2D-Game.git
$ cd Simple-SFML-2D-Game
$ mkdir build 
$ cd build
$ cmake -G "MinGW Makefiles" ..
$ mingw32-make
```

An .exe file should now exist in the ```build``` folder called **ScrollOfTheUndead.exe**.

## Details
This is game is an improvement of the book's **Chapter 7**. More specifically the following additions have been made:
- Added a healthbar for the player.
- Added a new spritesheet for the player.
- Added music and sounds (not with the book's sound manager but with a much less sophisticated implementation)
- ~Added a new tileset (16 * 16)~ Added an new Tile Set (32x32).
- Added a Python script that generates .map files from .csv files made with <a href="https://www.mapeditor.org/" target="_blank">Tiled</a> (This makes it easier to create a map)
- Added **CMakeLists.txt** a based on <a href="https://dane-bulat.medium.com/cmake-building-sfml-and-game-projects-on-linux-3947b3ba6e8" target="_blank">this</a> amazing guide.
- Minor other changes...

This project started because I wanted to create a video game from scratch. Thankfully the book does a good job providing and explaining a template that can be a good start as my very first game. I strongly recommend you check out this book if you want to see what game development really is.

I chose Chapter 7 as I feel it is a good middle ground for everyone how have read the book. Do not expect this to be the most amazing game ever.

Before checking out the source code I strongly recommend to read the book first (especially if you are relatively new to C++ like me). There is also documentation (in Greek) provided in the **docs** folder.

## Assets used

1. Textures:
    - Necromancer sprites: https://creativekind.itch.io/necromancer-free - Author: CreativeKind
    - Enemy sprites: https://luizmelo.itch.io/monsters-creatures-fantasy - Author: LuizMelo
    - Tileset 16x16 (not used currently): https://poloviiinkin.itch.io/textures - Author: Poloviiinkin
    - Tileset 32x32 (this is the one used by the game): https://opengameart.org/content/dungeon-crawl-32x32-tiles - Author: Chris Hamons
    - Heart sprites: https://nicolemariet.itch.io/pixel-heart-animation-32x32-16x16-freebie - Author: NicoleMarieT
    - HUD Sprite: https://dandann1.itch.io/hud-buttons - - Author: DanDann1
2. Music:
    - https://freepd.com/world.php
    - https://freepd.com/horror.php
    - https://freepd.com/epic.php
3. Sound effects: 
    - from https://pixabay.com
        - Knife slice - Author: NeoSpica
        - Bone Crack - Author: Universfield
        - attack cannibal beast - Author: jvmyka@gmail.com
        - transition explosion - Author: Cristian Changing
        - shield guard - Author: nekoninja
        - Interface - Author: Universfield
        - Failfare - Author: Wagna
        - coin 2 - Author: soundnimja
    - from https://opengameart.org
        - [Sound effects Pack 2](https://opengameart.org/content/sound-effects-pack-2) - Author: phoenix1291 
        - [Level up sound effects](https://opengameart.org/content/level-up-sound-effects) - Author: bart 
4. Backgrounds:
    - https://ansimuz.itch.io/mountain-dusk-parallax-background - Author: ansimuz
5. Fonts:
    - All fonts in the game's Resources are from https://www.dafont.com/
6. Logo made with <a href="https://placeit.net" target="_blank">placeit.net</a>

Huge shout out to all those amazing creators!

## Tools used
- <a href="https://libresprite.github.io/#!/" target="_blank">Libresprite</a>
- <a href="https://www.gimp.org/" target="_blank">Gimp</a>
- <a href="https://www.audacityteam.org/" target="_blank">Audacity</a>
- <a href="https://www.mapeditor.org/" target="_blank">Tiled</a>


## Important
I do **NOT** own the mentioned book, and this project is not made to be sold in any way.

## License
GPL-3.0 license - Check the [LICENSE.md](https://github.com/mataktelis11/Simple-SFML-2D-Game/blob/master/LICENSE.md) file.

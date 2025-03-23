# Welcome to the BlasterHacks 2025 Example Project

This project is meant to be a starting point for anyone who doesn't have experience coding. It will cover a bunch of topics to help you get started at this hackathon. While we would prefer this to be more a of areference for you to gain technical insights and tips as you build your own project, feel free to build this as your project with your own unique twists if you so choose.


Before we jump into building our demo project and learning about all the tools to hlpe you succeed I'd like to put a little disclaimer, this guide was written on a Mac. All tools, code, and tricks were tested on a Mac, so if you are on Windows or Linux be warned this isn't tested (but it should all still work).


Jump to any of the following sections:

- [Tools](#tools)
  - [Git](#git)
  - [Visual Studio Code](#visual-studio-code)
  - [Python](#python)
  - [Docker (advanced)](#docker-advanced)

# Tools

Before we get started with our super cool project, there are some helpful tools that will set your team up for success.

## Git

Git is a source control tool that will allow you to share code and keep track of changes. We will have more information on using git further into the guide, for now let's just make sure it is installed. Follow the [official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for specific instructions on how to install git.

Once you have completed the instructions for your operating system, open a terrminal and run `git --version` to verify you have installed git.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

So long as you are on an up to date Windows 11 installation you should have WinGet available.

To install Git with WinGet run the following command from powershell:

```ps1
winget install -e --id Git.Git
```

</details>

<details> 
<summary>Mac</summary>

On Mac, installing form the terminal requires Homebrew which you need to install if you haven't already.

<details>
<summary>Install Homebrew</summary>

To install Homebrew run the following command from your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

</details>

Once you have Homebrew installed it is as simple as opening a terminal and running:

```bash
brew install git
```

</details>

<details> 
<summary>Linux</summary>

Assuming you are on a Debian Linux distribution run:

```bash
apt install git
```

If you are on another distribution family, find the relevant command for your package manager.

</details>



## Visual Studio Code

Visual Studio Code (VSCode) is going to be our text editory of choice. Download it from the [official site](https://code.visualstudio.com/download). While any text editor will do I think VSCode is arguably the best free text editor for development.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In Powershell run:

```ps1
winget install -e --id Microsoft.VisualStudioCode
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install --cask visual-studio-code
```

</details>

<details> 
<summary>Linux</summary>

First add the apt repository.

To manually install the apt repository run the following commands.

```bash
sudo apt-get install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
rm -f packages.microsoft.gpg
```

To automatically install the apt repository run:

```bash
echo "code code/add-microsoft-repo boolean true" | sudo debconf-set-selections
```

Then update our package cache and install our package:

```bash
sudo apt install apt-transport-https
sudo apt update
sudo apt install code # or code-insiders
```

</details>

## Python

For this project I used Python 3.12 but any version from 3.10 onwards should be perfectly fine. If you need to install a new copy of Python, definitely go for Python 3.13. That said the [Python downloads page](https://code.visualstudio.com/download) should have the most recent stable release for your system available to download right at the top of hte page.

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In powershell run:

```ps1
winget install -e --id Python.Python.3
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install python
```

</details>

<details> 
<summary>Linux</summary>

In your terminal run:

```bash
sudo apt install python3 python3-pip
```

</details>

## Docker (Advanced)

Docker is a really cool tool used in industry for consistency, security, and scalability. Throughout this tutorial I will show the development process of this project with and without Docker. Docker will make our lives easier in a lot of ways, but it is another layer of complexity, so while I'd reccomend following the tutorial with it, feel free to skip it. Download it from the [official website](https://www.docker.com/get-started/) by hitting the download docker desktop button.  

Or install from the command line based on your operating system.

<details> 
<summary>Windows</summary>

In powershell run:

```ps1
winget install -e --id Docker.DockerDesktop
```

</details>

<details> 
<summary>Mac</summary>

In your terminal run:

```bash
brew install docker
```

</details>

<details> 
<summary>Linux</summary>

First uninstall any potential conflicting packages by running:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Then set up Docker's official apt repository:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Then install Docker:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

</details>
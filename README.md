# Converter_py-ipynb-md
Converter : Python file(.py) , Jupyter Notebook file (.ipynb), Markdown file(.md)

# Install
1. R language(3.0 + )

2. R Package
```R
install.packages("devtools")
devtools::install_github("mkearney/rmd2jupyter")
#1
```
3. Python language(3.6 + )

4. Python library
```
sudo -i
curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
python3 /tmp/get-pip.py
python3 -m pip install 'jupyter_contrib_nbextensions'
python3 -m pip install nbconvert
```

5. OS Package
```
# OS X
brew install coreutils
# Debian, Ubuntu, Kali Linux, Raspbian
apt-get install coreutils
# CentOS
yum install coreutils
# Alpine
apk add coreutils
# Arch Linux
pacman -S coreutils
# Fedora
dnf install coreutils
```

6. Install Script
```
git clone https://github.com/Finfra/Converter_py-ipynb-md.git
cd Script
. install.sh
cd ..
```

# Usage 1 : One File
![Command Map](img/CommandMap.png)
![Usage1](img/usage1.png)
![Usage1](img/usage2.png)
```
cd test
ls
p2j  a.py
ls
j2m a.ipynb
ls
cp a.md b.md
m2p b.md
ls
cp b.py c.py
p2m c.py
m2j c.md
cp c.ipynb d.ipynb
ls
j2p d.ipynb
ls
```

# Usage 2 : Batch
## Convert All Jupyter Notebook file to Markdown file.
```
. Converter_py-ipynb-md/Script/j2mAll.sh ..
```

## Convert All Markdown file to Jupyter Notebook file
```
./Converter_py-ipynb-md/Script/m2jAll ..  # It works if a md file is more last version then a ipynb file.
# or
./Converter_py-ipynb-md/Script/m2jAll .. -f
```


# Todo
* Install Manual for MS Windows
* Markdown 생성 될때 ipynb파일의 각 셀의 결과까지 저장되는 문제 해결
  - 해당 파일을 다시 ipynb파일로 바꾸면 셀의 실행 결과와 목차들이 붙는 문제가 있음.
  - 즉, 정확히 원복되지 않음.

# Cf
## Library Used
![Library Used](img/LibraryUsed.png)

# Made by [Finfra Co., Ltd](http://finfra.com)

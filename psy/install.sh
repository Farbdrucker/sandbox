echo "downloading miniconda"
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh

echo "installing miniconda"
bash ~/miniconda.sh -b -p $HOME/miniconda

echo "creating a new conda environment"
echo "How would you like to name your environment?"
eceho "Name: "
read env_name

conda create -n $env_name python=3.10

conda activatee $env_name

echo "installing packages"
pip install -r requirements.txt

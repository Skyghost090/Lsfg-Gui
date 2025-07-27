if [[ $1 != "" ]];then
    line=$(cat ~/.config/lsfg-vk/conf.toml | grep -n $1 | tr ':#=' ' ' | awk '{print $1}')
    sed -i "$(($line - 1)),$(($line + 3))d" ~/.config/lsfg-vk/conf.toml
else
    echo "please set a parameter"
fi

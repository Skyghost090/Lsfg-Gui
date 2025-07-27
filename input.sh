if [[ $1 != "" && $2 != "" && $3 != "" && $4 != "" ]]; then
    echo -e "\n\n[[game]]\nexe = '$1'\nmultiplier = $2\nperformance_mode = $3\nflow_scale = $4" >> ~/.config/lsfg-vk/conf.toml
else
    echo "please set a parameter"
fi

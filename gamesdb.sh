cat ~/.config/lsfg-vk/conf.toml | grep exe | awk '{print $3}' | tr = ' '| rev | cut -c2- | rev | cut -c2- | sed '1d' > games.txt

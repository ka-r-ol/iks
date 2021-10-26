echo "Commands: "
# base_dir=/Users/aiwon/.iks/menu
base_dir=$IKS_MENU_DIR
start_idx=$((${#base_dir}+2))
items=($(find $base_dir -name '*__*__item*' -type file -exec echo "{}" \; | cut -c${start_idx}-))

for item in "${items[@]}"; { 
  # echo "$item"; 
  IFS='/' read -r -a array <<< "$item";
  for element in "${array[@]}"; {
      label=$(echo $element | sed 's/__/;/g' | cut -d';' -f 1)
      printf " $label"
  }
  echo 

 # manage_full_path $item
}


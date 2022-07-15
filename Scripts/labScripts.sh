#!/bin/bash
menu() {
  echo "DANH MỤC LỰA CHỌN"
  echo "1 = Tạo thư mục mới"
  echo "2 = Xóa thư mục"
  echo "3 = Tạo file mới"
  echo "4 = Xóa file"
  echo "5 = Thoát"
}

xu-ly-menu(){
  flag=true
  chon=0
  while [[ $flag == true ]]
  do 
    menu
    echo "Mời chọn >>"
    read chon
    case $chon in
      1)
        echo -n "Vui lòng nhập tên folder cần tạo"; printf '\n'
        read tenFolder
        if [ ! -d "./${tenFolder}" ]; then
          mkdir  ${tenFolder}
        else 
          echo -n "Tên thư mục đã tồn tại"; printf '\n'
        fi
        
        ;;
      2)
        echo -n "Vui lòng nhập tên folder cần xóa"; printf '\n'
        read tenFolderXoa
        if [ ! -d "./${tenFolderXoa}" ]; then
          echo -n "Tên thư mục không tồn tại"; printf '\n'
        else 
          rm -rf  ${tenFolderXoa} 
        fi
        
        ;;
      3)
        echo -n "Vui lòng nhập tên files cần tạo"; printf '\n'
        read tenFile
        if [ ! -f "./${tenFile}" ]; then
          touch  ${tenFile}
        else 
          echo -n "Tên file đã tồn tại"; printf '\n'
        fi
        
        ;;
      4)
        echo -n "Vui lòng nhập tên file cần xóa"; printf '\n'
        read tenFileXoa
        if [ ! -f "./${tenFileXoa}" ]; then
          echo -n "Tên file không tồn tại"; printf '\n'
        else 
          rm -rf  ${tenFileXoa} 
        fi
        
        ;;
      5)
        flag=false
        
        ;;
      *)
        echo -n "Vui lòng chọn từ 1->5"; printf '\n'
    esac
  done
}

xu-ly-menu
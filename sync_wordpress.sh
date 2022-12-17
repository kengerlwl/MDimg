git_ans=$(git pull)
#git_ans='dat8987e'
grep_ans=$(echo $git_ans | grep date)
if [[  $grep_ans != "" ]]
then
  echo $git_ans
else
  echo "仓库文件更新，开始同步"
  python wordpress.py
fi
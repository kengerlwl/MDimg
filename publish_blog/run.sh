# 复制相关文档到带上传文件夹
rm -rf source/_posts
mkdir source/_posts
cp -rf ../copyMD/* ./source/_posts/

# 生成静态页面
hexo clean
hexo g
cd public


# # 初始化
# git init

# # 设置账号
# git config user.name "name"
# git config user.email "email"

# # commit
# git add .
# git commit -m "$(date) Update from Action"

# # 本地切换分支
# git branch gh-pages 
# git checkout gh-pages 

# # 强制上传
# git push --force --quiet "https://kengerlwl:${GITHUB_TOKEN}@github.com/kengerlwl/kengerlwl.github.io.git"  gh-pages    

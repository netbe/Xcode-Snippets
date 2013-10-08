#! /bin/bash
# source: https://github.com/iiiyu/oh-my-CodeSnippet
echo "Backing up snippets to: ~/Library/Developer/Xcode/UserData/CodeSnippets.backup"
mv ~/Library/Developer/Xcode/UserData/CodeSnippets ~/Library/Developer/Xcode/UserData/CodeSnippets.backup

# rm ~/Library/Developer/Xcode/UserData/CodeSnippets
echo "installing new ones"
SRC_HOME=`pwd`
ln -s ${SRC_HOME} ~/Library/Developer/Xcode/UserData/CodeSnippets
echo "done"

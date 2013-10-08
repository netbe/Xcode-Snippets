** Inspired by git@github.com:jaydee3/CodeSnippets.git **# CodeSnippets

These are my Xcode 4 CodeSnippets.  
To use them, clone this repository into the following path:

    cd ~/Library/Developer/Xcode/UserData/CodeSnippets
    git clone git@github.com:netbe/Xcode-Snippets.git .

(The folder must be empty, to clone the repository directly in it.)  
And you're ready to go.

#### Installing the pre-commit hook  
This README is generated automatically using `.generateDescription.py`.  
To run this script automatically before each commit, install the pre-commit hook like this:

    sh .install-precommit-hook.sh

## Snippet Descriptions

**enum.codesnippet**  (enum)  
Shortcut: `nsenum`  


    typedef NS_ENUM(<#type#>, <#name#>>) {
        <#value1#>,
        <#value2#>
    };

**stringConstant.codesnippet**  (String constant)  
Shortcut: `constStr`  


    NSString *const k<#constant#> = @"<#constant#>";

**strongProperty.codesnippet**  (Strong property)  
Shortcut: `ppstrong`  


    @property(nonatomic, strong)<#objectType#>* <#variable#>;

**weakself.codesnippet**  (weakSelf)  
Shortcut: ``  


    __weak __typeof(&*self)weakSelf = self;


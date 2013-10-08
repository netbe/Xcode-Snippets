# CodeSnippets

**Inspired by [jaydee3](https://github.com/jaydee3/CodeSnippets)**

These are my Xcode 4+ CodeSnippets.  
To use them, clone this repository, and execute the command:

    ./setup.sh
And you're ready to go.

This README is generated automatically using `.generateDescription.py`.  
This script executes automatically before each commit (pre-commit hook). You can remove the hook like this:

    rm .git/hooks/pre-commit

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


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

**appVersionLabel.codesnippet**  (app version label)  
Shortcut: `appversion`  


        NSDictionary *infoDictionary = [[NSBundle mainBundle] infoDictionary];
        NSString *version = [infoDictionary objectForKey:@"CFBundleShortVersionString"];
        NSString *build = [infoDictionary objectForKey:@"CFBundleVersion"];
        NSString *infos = [NSString stringWithFormat:@"v.%@ (build %@)",
                           version, build];
        
        UILabel *versionInfo = [[UILabel alloc] init];
        versionInfo.text = infos;
    

**callnumber.codesnippet**  (callNumber)  
Shortcut: `callNumber`  


    NSString* phoneNumberEscaped = <#phoneNumberString#>;
    // TODO escape string
                /**
                  componentsSeparatedByCharactersInSet:[[NSCharacterSet characterSetWithCharactersInString:@"0123456789"] invertedSet]] componentsJoinedByString:@""]
                 */
                
                NSString* callString = [NSString stringWithFormat:@"tel:%@", phoneNumberEscaped];
                [[UIApplication sharedApplication] openURL:[NSURL URLWithString:callString]];
    

**debugContext.codesnippet**  (debug Context)  
Shortcut: ``  
Logs for CoreData Context

    NSLog(@"Context: %@",<#writeContext#>);
                                            NSLog(@"PS Coord : %@",<#writeContext#>.persistentStoreCoordinator);
                                            NSLog(@"MOM : %@", <#writeContext#>.persistentStoreCoordinator.managedObjectModel);
                                            NSLog(@"Entities : %@",[[<#writeContext#>.persistentStoreCoordinator.managedObjectModel entities] valueForKey:@"name"]);

**enum.codesnippet**  (enum)  
Shortcut: `nsenum`  


    typedef NS_ENUM(<#type#>, <#name#>>) {
        <#value1#>,
        <#value2#>
    };

**hockeySetupPart.codesnippet**  (Hockey Setup part 2)  
Shortcut: `hockey-3`  


        [self configureHockey];

**stringConstant.codesnippet**  (String constant)  
Shortcut: `constStr`  


    NSString *const k<#constant#> = @"<#constant#>";

**strongProperty.codesnippet**  (Strong property)  
Shortcut: `ppstrong`  


    @property(nonatomic, strong)<#objectType#>* <#variable#>;

**viewMethods.codesnippet**  (View Methods)  
Shortcut: `viewimp`  


    #pragma mark - Layout
    
    -(void)addLayout
    {
    
    }
    
    #pragma mark - Lifecycle
    
    - (id)initWithFrame:(CGRect)frame
    {
        self = [super initWithFrame:frame];
        if (self) {
            // Initialization code
            [self addLayout];
        }
        return self;
    }
    

**visualconstraint.codesnippet**  (visualconstraint)  
Shortcut: `vct`  


     [<#view#> addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"<#code#>"
                                                                                 options:0
                                                                                 metrics:nil
                                                                                   views:views]];

**weakSelf.codesnippet**  (__weak self)  
Shortcut: `weak`  
Declare weak reference to self

    __weak __typeof(&*self)weakSelf = self;
    


# RecommenderAPI

Allows a user to upload a file of customer actions, navigate the execution flow in the browser, and have recommendations file saved to user's Download folder.

To run the application on local, just run the `run.py` file:

```
python run.py
```

The action format be in long format, for example:

```
user_id,item_id
Amy,C
Brian,Ruby
Chris,Java
Chris,Scala
Amy,Rust
Brian,Python
Dan,Rust
Emily,Python
Fred,Kotlin
Fred,Java
Emily,Lua
Dan,D
```

The RecommenderAPI will use Singular Value Decomposition algorithm to generate these recommendations:

```
Amy,Rust,D,C  
Brian,Python,Ruby,Lua
Chris,Java,Scala,Kotlin
Dan,Rust,D,C  
Emily,Python,Ruby,Lua
Fred,Java,Scala,Kotlin
```

The example is very much a softball, but the algorithm does figure out to make 3rd recommendation a correct language type. E.g, Amy clicked on Rust and C, which are low level languages and is recommended D, which is another low level language. The connections here mostly works though Dan who clicked on Rust and D. 
``` mermaid
flowchart TD;
    A([Start]) ---> B{What is it};
    B -->|Object| C[Create a Node];
    B -->|Connection| D[Create a Link];
    C --> E{What kind of object};
    E -->|Specific Named Object| F[Group: Proper];
    E -->|Common Object| G[Group: Common];
```

# ES6 Modules

Modules are essentially putting code into separate files that you can export and import for reuse purposes.

Usage:

```
const functionOne = () => console.log('FUNCTION ONE!');

export { functionOne };
```

```
import { functionOne } from './functionOne';

functionOne();
```

Good references:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export

<h3>Exports</h3>

There are two types of exports: named and default.

Named Exports:
- Syntax: export { myFunction }
- Named exports must be imported with the same name, but can be given an alias.
- During import, they must be imported in curly braces with the same name

Default Exports:
- Syntax: export default someFunction 
- Default exports can be imported with any name. 
- You can only have one.
 
 <h3>Imports</h3>

 Named Imports:
 - Syntax: import { myFunction } from './file'

 Default Imports:
 - Syntax: import someFunction from './file'
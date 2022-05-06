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
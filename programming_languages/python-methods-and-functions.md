### 1. Built-in Functions (The Logic Engines)

These are global functions used to transform, evaluate, or inspect data structures.

| Function | Syntax | Purpose / Explanation | Example |
| --- | --- | --- | --- |
| **`map()`** | `map(func, iter)` | Applies a function to every item in an iterable. Returns a generator. | `list(map(str.upper, ['a', 'b']))` |
| **`filter()`** | `filter(func, iter)` | Filters an iterable based on a function that returns `True/False`. | `filter(lambda x: x > 0, nums)` |
| **`sorted()`** | `sorted(iter, key, rev)` | Unlike `.sort()`, this returns a **new** sorted list without modifying the original. | `new_list = sorted(data)` |
| **`zip()`** | `zip(*iters)` | Pairs elements from multiple iterables into tuples. Great for dict creation. | `dict(zip(keys, values))` |
| **`enumerate()`** | `enumerate(iter, start)` | Returns pairs of `(index, element)`. Essential for clean `for` loops. | `for i, val in enumerate(list):` |
| **`any()` / `all()**` | `any(iter)` | `any`: True if one is true. `all`: True if all are true. Logical short-circuiting. | `if all(status == "OK"):` |
| **`dir()`** | `dir(obj)` | **Introspection:** Returns a list of all valid attributes and methods for an object. | `dir(str)` |
| **`isinstance()`** | `isinstance(obj, type)` | Checks if an object belongs to a class. Preferred over `type(obj) == ...`. | `isinstance(data, dict)` |

---

### 2. Core Object Methods (The Data Transformers)

Methods called directly on String, List, and Dictionary objects.

| Method | Syntax | Purpose / Explanation | Example |
| --- | --- | --- | --- |
| **`.get()`** | `dict.get(key, def)` | Accesses dict values safely. No `KeyError` if the key is missing. | `val = my_dict.get("id", 0)` |
| **`.update()`** | `dict.update(other)` | Merges another dictionary or iterable of pairs into the current one. | `settings.update(new_config)` |
| **`.join()`** | `'sep'.join(iter)` | Merges a list of strings into one string. High performance for large data. | `", ".join(user_emails)` |
| **`.strip()`** | `s.strip([chars])` | Cleans up leading/trailing whitespace or specific unwanted characters. | `"  clean me  ".strip()` |
| **`.pop()`** | `list.pop(index)` | Removes and returns the item at a specific index (default is last). | `last_task = queue.pop(0)` |
| **`.extend()`** | `list.extend(iter)` | Appends all elements of an iterable to the list (vs `.append()` which adds the whole list). | `my_list.extend([4, 5, 6])` |

---

### 3. Advanced Context & Identity

| Tool | Syntax | Purpose / Explanation | Example |
| --- | --- | --- | --- |
| **`set()`** | `set(iterable)` | Function to convert to a set. Used to remove duplicates instantly. | `unique = list(set(duplicates))` |
| **`id()`** | `id(obj)` | Returns the unique identity (memory address) of an object. | `if id(a) == id(b):` |
| **`help()`** | `help(obj)` | Invokes the built-in help system for any function or module. | `help(sorted)` |
| **`round()`** | `round(num, ndig)` | Rounds a number to a specified number of decimals. | `round(3.14159, 2)` |


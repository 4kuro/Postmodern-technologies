import { valueTypes, referenceTypes, referenceTypes2, modifyObject, modifyArray, addAndPop } from './functions';
var gc = require("js-gc")


test('should garbage collect unused objects', () => {
  let obj: any = {data: "Bob"};
  const before = process.memoryUsage().heapUsed;
  obj = null;
  gc();
  const after = process.memoryUsage().heapUsed;
  const res = after - before;
  expect(res).toBeLessThan(0); 
});

test('heap object check', () => {
  const before = process.memoryUsage().heapUsed;
  let obj = "Alice";
  const result = process.memoryUsage().heapUsed - before;
  expect(result).toBeGreaterThan(0);
  })


  test('valueTypes should demonstrate value type behavior', () => {
    const { a, b } = valueTypes();
    expect(a).toBe(10);
    expect(b).toBe(20);
  });
  
  test('modifyObject should modify object reference', () => {
    const obj = { name: 'Alice' };
    modifyObject(obj, 'Bob');
    expect(obj.name).toBe('Bob');
  });
  
  test('modifyArray should modify array reference', () => {
    const arr = [1, 2, 3];
    modifyArray(arr, 0, 10);
    expect(arr[0]).toBe(10);
  });
  
  test('modifyObject should not modify object value type', () => {
    const { obj1 } = referenceTypes();
    const originalName = obj1.name;
    modifyObject(obj1, 'Charlie');
    expect(obj1.name).toBe(originalName); // Повинно бути fail щоб довести, що об'єкти передаються по ссилці а не по значенню
  });
  
  test('modifyArray should not modify array value type', () => {
    const { arr1 } = referenceTypes2();
    const originalValue = arr1[0];
    modifyArray(arr1, 0, 10);
    expect(arr1[0]).toBe(originalValue); // Значення не повинно змінитися
  });


  test('should demonstrate stack behavior', () => {
    const stack: any[] = [1, 2, 3];
    const beforeSize = stack.length;

    const result = addAndPop(stack); // Tест показує що список працює на стеку

    const afterSize = result.newArr.length;
    const poppedValue = result.poppedValue;

    expect(afterSize).toBe(beforeSize);
    expect(poppedValue).toBe(1);
  });

  test('stack object check', () => {
    const before = process.memoryUsage().heapUsed;
    let n = 5;
    const result = process.memoryUsage().heapUsed - before;
    expect(result).toBe(0);
  })
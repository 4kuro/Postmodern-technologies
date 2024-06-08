//variant 1
import { valueTypes, referenceTypes, referenceTypes2} from './functions';
import { modifyObject, modifyArray } from './functions';

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

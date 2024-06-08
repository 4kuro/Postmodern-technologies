// variant 1
export function valueTypes() {
    let a: number = 10; // примітивний тип зберігається на стеку
    let b: number = a; // b отримує копію значення a
    b = 20; // зміна b не впливає на a
    return { a, b };
  }

   export function referenceTypes() {
    let obj1 = { name: "Alice" }; // об'єкт створюється в хіпі
    let obj2 = obj1; // obj2 отримує посилання на obj1
    obj2.name = "Bob"; // зміна obj2 впливає на obj1, оскільки обидва посилаються на той самий об'єкт
    return { obj1, obj2 };
  }
  
  export function referenceTypes2() {
    let arr1 = [1, 2, 3];
    let arr2 = arr1; // arr2 отримує посилання на arr1
    arr2[0] = 10; // зміна arr2 впливає на arr1
    return { arr1, arr2 };
  }
  
  export function modifyObject(obj: any, newValue: string) {
    obj.name = newValue;
  }
  
  export function modifyArray(arr: any[], index: number, newValue: number) {
    arr[index] = newValue;
  }
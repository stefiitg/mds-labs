// Introduction
method Double(x: int) returns (y: int)
  ensures y == 2 * x
{
  y := x + x;
}

// Exercise 1: Absolute Value
method Abs(x: int) returns (y: int)
  ensures y >= 0
  ensures y == x || y == -x
{
  if x < 0 {
    y := -x;
  } else {
    y := x;
  }
}

// Division
method Divide(x: int, y: int) returns (r: int)
  requires y != 0
  ensures r == x / y
{
  r := x / y;
}

// Exercise 2: Max
method Max(x: int, y: int) returns (m: int)
  ensures m >= x && m >= y
  ensures m == x || m == y
{
  if x > y {
    m := x;
  } else {
    m := y;
  }
}

// Weak Max
method MaxWeak(x: int, y: int) returns (m: int)
  ensures m >= x && m >= y
{
  m := x + y + 1; // not a max, but Dafny accepts it!
}

// Exercise 3: Strengthen the Specification
// Note: Dafny va raporta o eroare intenționată aici deoarece implementarea este greșită, 
// dar specificația este acum corectă/puternică!
method MaxWeakFixed(x: int, y: int) returns (m: int)
  ensures m >= x && m >= y
  ensures m == x || m == y
{
  m := x + y + 1; 
}

// Exercise 4: Specify the Bank Transfer
method TransferSpec(a: int, b: int, amount: int) returns (a2: int, b2: int)
  requires a >= 0 && b >= 0
  requires amount > 0
  requires a >= amount
  ensures a2 + b2 == a + b
  ensures a2 >= 0 && b2 >= 0
{
  a2 := a - amount;
  b2 := b + amount;
}

// Exercise 5: Unsafe Access
// Note: Dafny va raporta eroare aici (index out of range) deoarece lipsește `requires 0 <= i < arr.Length`
method GetAtUnsafe(arr: array<int>, i: int) returns (x: int)
{
  x := arr[i]; 
}

// Loop Invariants Example
method Sum(n: int) returns (s: int)
  requires n >= 0
  ensures s == n * (n + 1) / 2
{
  s := 0;
  var i := 0;
  // Fără invarianți, dă eroare
  while i <= n
    invariant 0 <= i <= n + 1
    invariant s == i * (i - 1) / 2
  {
    s := s + i;
    i := i + 1;
  }
}

// Exercise 6: Add Loop Invariants to SumFixed
method SumFixed(n: int) returns (s: int)
  requires n >= 0
  ensures s == n * (n + 1) / 2
{
  s := 0;
  var i := 0;
  while i <= n
    invariant 0 <= i <= n + 1
    invariant s == i * (i - 1) / 2
  {
    s := s + i;
    i := i + 1;
  }
}

// Exercise 7: MaxArrayFixed
method MaxArrayFixed(arr: array<int>) returns (m: int)
  requires arr.Length > 0
  ensures forall i :: 0 <= i < arr.Length ==> m >= arr[i]
{
  m := arr[0];
  var i := 1;
  while i < arr.Length
    invariant 1 <= i <= arr.Length
    invariant forall k :: 0 <= k < i ==> m >= arr[k]
  {
    if arr[i] > m {
      m := arr[i];
    }
    i := i + 1;
  }
}

@number = global i32 10

define void @foo() {
  %arr = alloca [10 x i32]
  %1 = load i32, i32* @number
  %2 = getelementptr inbounds [10 x i32],
       [10 x i32]* %a, i64 0, i64 5
  store i32 %1, i32* %2
  ret void
}

define i32 @main() {
  %1 = alloca i32
  store i32 0, i32* %1
  call void @foo()
  ret i32 0
}



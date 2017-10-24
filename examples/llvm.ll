@number = global i32 10, align 4

define void @foo() {
  %a = alloca [10 x i32], align 16
  %1 = load i32, i32* @number, align 4
  %2 = getelementptr inbounds [10 x i32],
       [10 x i32]* %a, i64 0, i64 5
  store i32 %1, i32* %2, align 4
  ret void
}

define i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  call void @foo()
  ret i32 0
}



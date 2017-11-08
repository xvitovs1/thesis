@globalInteger = global i32 0, align 4

<@\vdots@>

<@{\color[RGB]{0,135,0} \%1 = bitcast i32* @globalInteger to i8*}@>
<@{\color[RGB]{0,135,0}  call void @\_\_INSTR\_remember\_global(i8* \%1, i64 4)}@>
%2 = alloca i32, align 4
<@{\color[RGB]{0,135,0}  \%3 = bitcast i32* \%2 to i8*}@>
<@{\color[RGB]{0,135,0}  call void @\_\_INSTR\_remember(i8* \%3, i64 4, i32 1)}@>
%4 = alloca i32, align 4
<@{\color[RGB]{0,135,0}  \%5 = bitcast i32* \%4 to i8*}@>
<@{\color[RGB]{0,135,0}  call void @\_\_INSTR\_remember(i8* \%5, i64 4, i32 1)}@>
store i32 5, i32* %2, align 4
store i32 10, i32* %4, align 4
%6 = load i32, i32* %2, align 4
%7 = load i32, i32* %4, align 4
%8 = add nsw i32 %6, %7
store i32 %8, i32* @globalInteger, align 4



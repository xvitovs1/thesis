%1 = alloca [10 x i32]
<@{\color[RGB]{0,135,0} \%2 = bitcast [10 x i32]* \%1 to i8*}@>
<@{\color[RGB]{0,135,0} call void \@\_\_INSTR\_remember(i8* \%2, i64 40, i32 1)}@>
%3 = getelementptr inbounds [10 x i32], [10 x i32]* %1,
      i64 0, i64 0
store i32 1, i32* %3
%4 = getelementptr inbounds [10 x i32], [10 x i32]* %1,
      i64 0, i64 20
<@{\color[RGB]{0,135,0} \%5 = bitcast i32* \%4 to i8*}@>
<@{\color[RGB]{0,135,0} call void \@\_\_INSTR\_check\_pointer(i8* \%5, i64 4)}@>
store i32 1, i32* %4


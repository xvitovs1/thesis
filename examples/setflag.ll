define i32* @getArray() {
  <@{\color[RGB]{0,135,0} call void \@\_\_INSTR\_set\_flag()}@>
  %1 = alloca [10 x i32]
  <@{\color[RGB]{0,135,0} \%2 = bitcast [10 x i32]* \%1 to i8*}@>
  <@{\color[RGB]{0,135,0} call void \@\_\_INSTR\_remember(i8* \%2, i64 40, i32 1)}@>
  %3 = getelementptr inbounds [10 x i32], [10 x i32]* %1,
        i32 0, i32 0
  <@{\color[RGB]{0,135,0} call void \@\_\_INSTR\_destroy\_allocas()}@>
  ret i32* %3
}


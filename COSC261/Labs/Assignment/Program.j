.class public Program
.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method
.method public static main([Ljava/lang/String;)V
.limit locals 5
.limit stack 1024
new java/util/Scanner
dup
getstatic java/lang/System.in Ljava/io/InputStream;
invokespecial java/util/Scanner.<init>(Ljava/io/InputStream;)V
astore 0
aload 0
invokevirtual java/util/Scanner.nextInt()I
istore 1
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 1
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
sipush 0
istore 2
sipush 0
istore 3
l1:
iload 1
sipush 0
if_icmplt l4
iload 1
sipush 10
if_icmpgt l4
goto l3
l4:
goto l2
l3:
iload 1
sipush 10
if_icmpge l7
goto l6
l7:
goto l5
l6:
iload 1
sipush 8
if_icmpne l11
goto l10
l11:
goto l8
l10:
getstatic java/lang/System/out Ljava/io/PrintStream;
sipush 1
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
l8:
iload 2
iload 1
iadd
istore 2
l9:
l5:
iload 1
sipush 1
iadd
istore 1
goto l1
l2:
iload 2
istore 4
iload 4
sipush 25
if_icmpge l14
goto l13
l14:
goto l12
l13:
iload 4
istore 3
l12:
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 3
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
return
.end method

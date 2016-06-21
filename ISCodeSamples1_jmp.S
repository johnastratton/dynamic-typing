	.file	"ISCodeSamples1.cpp"
	.section	.text._ZN14sample_virtual6updateEv,"axG",@progbits,_ZN14sample_virtual6updateEv,comdat
	.align 2
	.p2align 4,,15
	.weak	_ZN14sample_virtual6updateEv
	.type	_ZN14sample_virtual6updateEv, @function
_ZN14sample_virtual6updateEv:
.LFB1099:
	.cfi_startproc
	movsd	.LC0(%rip), %xmm0
	addsd	8(%rdi), %xmm0
	movsd	%xmm0, 8(%rdi)
	ret
	.cfi_endproc
.LFE1099:
	.size	_ZN14sample_virtual6updateEv, .-_ZN14sample_virtual6updateEv
	.text
	.align 2
	.p2align 4,,15
	.type	_ZN13sample_member6updateEv.isra.0, @function
_ZN13sample_member6updateEv.isra.0:
.LFB1108:
	.cfi_startproc
	movsd	.LC0(%rip), %xmm0
	addsd	(%rdi), %xmm0
	movsd	%xmm0, (%rdi)
	ret
	.cfi_endproc
.LFE1108:
	.size	_ZN13sample_member6updateEv.isra.0, .-_ZN13sample_member6updateEv.isra.0
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.type	_Z41__static_initialization_and_destruction_0ii.constprop.1, @function
_Z41__static_initialization_and_destruction_0ii.constprop.1:
.LFB1109:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	jmp	__cxa_atexit
	.cfi_endproc
.LFE1109:
	.size	_Z41__static_initialization_and_destruction_0ii.constprop.1, .-_Z41__static_initialization_and_destruction_0ii.constprop.1
	.text
	.p2align 4,,15
	.globl	_Z10run_memberP13sample_member
	.type	_Z10run_memberP13sample_member, @function
_Z10run_memberP13sample_member:
.LFB1100:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	movl	$10, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	leaq	8(%rdi), %rbp
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	.p2align 4,,10
	.p2align 3
.L6:
	xorl	%ebx, %ebx
	.p2align 4,,10
	.p2align 3
.L9:
	leaq	0(%rbp,%rbx), %rdi
	addq	$16, %rbx
	call	_ZN13sample_member6updateEv.isra.0
	cmpq	$160000, %rbx
	jne	.L9
	subl	$1, %r12d
	jne	.L6
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1100:
	.size	_Z10run_memberP13sample_member, .-_Z10run_memberP13sample_member
	.p2align 4,,15
	.globl	_Z11run_virtualP14sample_virtual
	.type	_Z11run_virtualP14sample_virtual, @function

_Z11run_virtualP14sample_virtual:
.LFB1101:
	.cfi_startproc
	pushq	%r13
	.cfi_def_cfa_offset 16
	.cfi_offset 13, -16
	movq	%rdi, %r13
	pushq	%r12
	.cfi_def_cfa_offset 24
	.cfi_offset 12, -24
	movl	$10, %r12d
	pushq	%rbp
	.cfi_def_cfa_offset 32
	.cfi_offset 6, -32
	pushq	%rbx
	.cfi_def_cfa_offset 40
	.cfi_offset 3, -40
	subq	$8, %rsp
	.cfi_def_cfa_offset 48
	.p2align 4,,10
	.p2align 3
.L13:
	movq	%r13, %rbx
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L16:
	movq	(%rbx), %rax
	addl	$1, %ebp
	movq	%rbx, %rdi
	addq	$16, %rbx
	call 	.stub
	cmpl	$10000, %ebp
	jne	.L16
	subl	$1, %r12d
	jne	.L13
	addq	$8, %rsp
	.cfi_def_cfa_offset 40
	popq	%rbx
	.cfi_def_cfa_offset 32
	popq	%rbp
	.cfi_def_cfa_offset 24
	popq	%r12
	.cfi_def_cfa_offset 16
	popq	%r13
	.cfi_def_cfa_offset 8
	ret
.stub:
	jmp	*(%rax)
	.cfi_endproc
.LFE1101:
	.size	_Z11run_virtualP14sample_virtual, .-_Z11run_virtualP14sample_virtual
	.section	.text._ZN14sample_virtualC2Ev,"axG",@progbits,_ZN14sample_virtualC5Ev,comdat
	.align 2
	.p2align 4,,15
	.weak	_ZN14sample_virtualC2Ev
	.type	_ZN14sample_virtualC2Ev, @function
_ZN14sample_virtualC2Ev:
.LFB1104:
	.cfi_startproc
	movq	$_ZTV14sample_virtual+16, (%rdi)
	ret
	.cfi_endproc
.LFE1104:
	.size	_ZN14sample_virtualC2Ev, .-_ZN14sample_virtualC2Ev
	.weak	_ZN14sample_virtualC1Ev
	.set	_ZN14sample_virtualC1Ev,_ZN14sample_virtualC2Ev
	.section	.text.startup
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1102:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$160008, %rsp
	.cfi_def_cfa_offset 160032
	leaq	160000(%rsp), %rbp
	movq	%rsp, %rbx
	.p2align 4,,10
	.p2align 3
.L21:
	movq	%rbx, %rdi
	addq	$16, %rbx
	call	_ZN14sample_virtualC1Ev
	cmpq	%rbp, %rbx
	jne	.L21
#APP
# 88 "ISCodeSamples1.cpp" 1
	mov $1, %rax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	movq	%rsp, %rdi
	call	_Z11run_virtualP14sample_virtual
#APP
# 91 "ISCodeSamples1.cpp" 1
	mov $2, %rax
	xchg %bx, %bx

# 0 "" 2
#NO_APP
	addq	$160008, %rsp
	.cfi_def_cfa_offset 24
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE1102:
	.size	main, .-main
	.p2align 4,,15
	.type	_GLOBAL__sub_I__Z10run_memberP13sample_member, @function
_GLOBAL__sub_I__Z10run_memberP13sample_member:
.LFB1107:
	.cfi_startproc
	jmp	_Z41__static_initialization_and_destruction_0ii.constprop.1
	.cfi_endproc
.LFE1107:
	.size	_GLOBAL__sub_I__Z10run_memberP13sample_member, .-_GLOBAL__sub_I__Z10run_memberP13sample_member
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z10run_memberP13sample_member
	.weak	_ZTI14sample_virtual
	.section	.rodata._ZTI14sample_virtual,"aG",@progbits,_ZTI14sample_virtual,comdat
	.align 16
	.type	_ZTI14sample_virtual, @object
	.size	_ZTI14sample_virtual, 16
_ZTI14sample_virtual:
	.quad	_ZTVN10__cxxabiv117__class_type_infoE+16
	.quad	_ZTS14sample_virtual
	.weak	_ZTS14sample_virtual
	.section	.rodata._ZTS14sample_virtual,"aG",@progbits,_ZTS14sample_virtual,comdat
	.align 16
	.type	_ZTS14sample_virtual, @object
	.size	_ZTS14sample_virtual, 17
_ZTS14sample_virtual:
	.string	"14sample_virtual"
	.weak	_ZTV14sample_virtual
	.section	.rodata._ZTV14sample_virtual,"aG",@progbits,_ZTV14sample_virtual,comdat
	.align 16
	.type	_ZTV14sample_virtual, @object
	.size	_ZTV14sample_virtual, 24
_ZTV14sample_virtual:
	.quad	0
	.quad	_ZTI14sample_virtual
	.quad	_ZN14sample_virtual6updateEv
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC0:
	.long	0
	.long	1072693248
	.hidden	__dso_handle
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04) 4.8.4"
	.section	.note.GNU-stack,"",@progbits

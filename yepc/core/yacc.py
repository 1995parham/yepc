# In The Name Of God
# ========================================
# [] File Name : yacc.py
#
# [] Creation Date : 31-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
#
# [] Created By : Saman Fekri (samanf74@gmail.com)
# =======================================
import ply.yacc as yacc
from .lex import YEPCLexer


class YEPCParser:
    tokens = YEPCLexer.tokens

    precedence = (
        ('left', 'EXP_OP'),
        ('left', 'IF_KW', 'ELSE_KW'),
        ('left', 'OR_KW', 'AND_KW'),
        ('left', 'REL_OP'),
        ('left', 'MATH_OP'),
        ('left', 'NOT_KW')
    )

    def p_program(self, p):
        'program : declarationList'
        pass

    def p_declaration_list(self, p):
        '''
        declarationList : declarationList declaration
                        | declaration
        '''
        pass

    def p_declaration(self, p):
        '''
        declaration : varDeclaration
                    | funDeclaration
                    | recDeclaration
        '''
        pass

    def p_rec_declaration(self, p):
        '''
        recDeclaration : RECORD_KW ID BR_OPEN localDeclarations BR_CLOSE
        '''
        pass

    def p_var_declaration(self, p):
        '''
        varDeclaration : typeSpecifier varDeclarationList SEMICOLON
        '''
        pass

    def p_scoped_var_declaration(self, p):
        '''
        scopedVarDeclaration : scopedTypeSpecifier varDeclarationList SEMICOLON
        '''
        pass

    def p_var_declaration_list(self, p):
        '''
        varDeclarationList : varDeclarationList COMMA varDeclarationInitialize
                           | varDeclarationInitialize
        '''
        pass

    def p_var_declaration_initialize(self, p):
        '''
        varDeclarationInitialize : varDeclarationId
                                 | varDeclarationId COLON simpleExpression
        '''
        pass

    def p_var_declaration_id(self, p):
        '''
        varDeclarationId : ID
                         | ID BK_OPEN NUMCONST BK_CLOSE

        '''
        pass

    def p_scoped_type_specifier(self, p):
        '''
        scopedTypeSpecifier : STATIC_KW typeSpecifier
                            | typeSpecifier
        '''
        pass

    def p_type_specifier(self, p):
        '''
        typeSpecifier : returnTypeSpecifier
                      | ID
        '''
        pass

    def p_return_type_specifier(self, p):
        '''
        returnTypeSpecifier : INT_T
                            | REAL_T
                            | BOOL_T
                            | CHAR_T
        '''
        pass

    def p_fun_declaration(self, p):
        '''
        funDeclaration : typeSpecifier ID PR_OPEN params PR_CLOSE statement
                       | ID PR_OPEN params PR_CLOSE statement
        '''
        pass

    def p_params(self, p):
        '''
        params : paramList
               | empty
        '''
        pass

    def p_param_list(self, p):
        '''
        paramList : paramList SEMICOLON paramTypeList
                  | paramTypeList
        '''
        pass

    def p_param_type_list(self, p):
        '''
        paramTypeList : typeSpecifier paramIdList
        '''
        pass

    def p_param_id_list(self, p):
        '''
        paramIdList : paramIdList COMMA paramId
                    | paramId
        '''
        pass

    def p_param_id(self, p):
        '''
        paramId : ID
                | ID BK_OPEN BK_CLOSE
        '''
        pass

    def p_statement(self, p):
        '''
        statement : expressionStmt
                  | compoundStmt
                  | selectionStmt
                  | iterationStmt
                  | returnStmt
                  | breakStmt
        '''
        pass

    def p_compound_stmt(self, p):
        '''
        compoundStmt : BR_OPEN localDeclarations statementList BR_CLOSE
        '''
        pass

    def p_local_declarations(self, p):
        '''
        localDeclarations : localDeclarations scopedVarDeclaration
                          | empty
        '''
        pass

    def p_statement_list(self, p):
        '''
        statementList : statementList statement
                      | empty
        '''
        pass

    def p_expression_stmt(self, p):
        '''
        expressionStmt : expression SEMICOLON
                       | SEMICOLON
        '''
        pass

    def p_selection_stmt(self, p):
        '''
        selectionStmt : IF_KW PR_OPEN simpleExpression PR_CLOSE statement
                      | IF_KW PR_OPEN simpleExpression PR_CLOSE statement ELSE_KW statement
                      | SWITCH_KW PR_OPEN simpleExpression PR_CLOSE caseElement defaultElement END_KW
        '''
        pass

    def p_case_element(self, p):
        '''
        caseElement : CASE_KW NUMCONST COLON statement SEMICOLON
                    | caseElement CASE_KW NUMCONST COLON statement SEMICOLON
        '''
        pass

    def p_default_element(self, p):
        '''
        defaultElement : DEFAULT_KW COLON statement SEMICOLON
                       | empty
        '''
        pass

    def p_iteration_stmt(self, p):
        '''
        iterationStmt : WHILE_KW PR_OPEN simpleExpression PR_CLOSE statement
        '''
        pass

    def p_return_stmt(self, p):
        '''
        returnStmt : RETURN_KW SEMICOLON
                   | RETURN_KW expression SEMICOLON
        '''
        pass

    def p_break_stmt(self, p):
        '''
        breakStmt : BREAK_KW SEMICOLON
        '''
        pass

    def p_expression(self, p):
        '''
        expression : mutable EXP_OP expression
                   | mutable MATH_OP EXP_OP expression
                   | simpleExpression
                   | mutable MATH_OP MATH_OP
        '''
        pass

    def p_simple_expression(self, p):
        '''
        simpleExpression : simpleExpression OR_KW simpleExpression
                         | simpleExpression AND_KW simpleExpression
                         | simpleExpression OR_KW ELSE_KW simpleExpression
                         | simpleExpression AND_KW THEN_KW simpleExpression
                         | NOT_KW simpleExpression
                         | relExpression
        '''
        pass

    def p_rel_expression(self, p):
        '''
        relExpression : mathlogicExpression REL_OP mathlogicExpression
                      | mathlogicExpression
        '''
        pass

    def p_mathlogic_expression(self, p):
        '''
        mathlogicExpression : mathlogicExpression MATH_OP mathlogicExpression
                            | unaryExpression
        '''
        pass

    def p_unary_expression(self, p):
        '''
        unaryExpression : MATH_OP unaryExpression
                        | factor
        '''
        pass

    def p_factor(self, p):
        '''
        factor : immutable
               | mutable
        '''
        pass

    def p_mutable(self, p):
        '''
        mutable : ID
                | mutable BK_OPEN expression BK_CLOSE
                | mutable DOT ID
        '''
        pass

    def p_immutable(self, p):
        '''
        immutable : PR_OPEN expression PR_CLOSE
                  | call
                  | constant
        '''
        pass

    def p_call(self, p):
        '''
        call : ID PR_OPEN args PR_CLOSE
        '''
        pass

    def p_args(self, p):
        '''
        args : argList
             | empty
        '''
        pass

    def p_arg_list(self, p):
        '''
        argList : argList COMMA expression
                | expression
        '''
        pass

    def p_constant(self, p):
        '''
        constant : NUMCONST
                 | REALCONST
                 | CHARCONST
                 | TRUE
                 | FALSE
        '''
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input: %s" % p)

    # Empty rule
    def p_empty(self, p):
        '''
        empty :
        '''
        pass

    def build(self, **kwargs):
        '''
        build the parser
        '''
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

# -*- coding: utf-8 -*-

def index():
    
    hifen_attr={'_data-activates':"slide-out"}
    header=CAT(
                TAG['nav'](
                    DIV(
                        A("MINHA NOTA UNIT", _href=URL('www','index'), _class="brand-logo right minhanotaunit"),
                        UL(
                            LI(
                                UL(
                                    LI(
                                        H5("Configure os pesos", _style='text-align:center; text-transform:uppercase; color: black'),
                                        H6("(Composição da nota)", _style='text-align:center; text-transform:uppercase; color: grey')
                                        ),
                                    LI(
                                        DIV(_class="divider")
                                        ),
                                    BR(),
                                    LI(
                                        DIV(
                                            DIV(
                                                INPUT(_id="peso_prova", _type="tel", _class="validate eh_nota"),
                                                LABEL("Peso da Prova", _for="peso_prova"),
                                                _class="input-field col s12"),
                                            _class='row'),
                                        ),
                                    LI(
                                        DIV(
                                            DIV(
                                                INPUT(_id="peso_aas", _type="tel", _class="validate eh_nota"),
                                                LABEL("Peso das AAs", _for="peso_aas"),
                                                _class="input-field col s12"),
                                            _class='row'),
                                        ),
                                    LI(
                                        DIV(
                                            DIV(
                                                INPUT(_id="peso_pas", _type="tel", _class="validate eh_nota"),
                                                LABEL("Peso da PAS", _for="peso_pas"),
                                                _class="input-field col s12"),
                                            _class='row'),
                                        ),
                                    LI(
                                        DIV(_class="divider")
                                        ),
                                    LI(

                                        A("Sobre", _href=URL('www', 'sobre'))
                                        ),
                                    _id="slide-out", _class="side-nav", _style="color:black"),
                                A(
                                    I( _class="fa fa-bars"), 
                                    _href="#" , _class="button-collapse", **hifen_attr)
                                ),
                            _id="nav-mobile"),
                        _class="minhanotaunit nav_wrapper")
                    ),
                )

    main=DIV(
            UL(
                LI("Nota de Prova", _class="collection-header"),
                LI(

                    DIV(
                        INPUT(_id="nprova", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota da Prova", _for="nprova"),
                        _class="input-field"),

                    _class="collection-item"),
                LI("Nota das Atividades de Autoaprendizagem", _class="collection-header"),
                LI(
                    DIV(
                        INPUT(_id="aa1", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota AA1", _for="aa1"),
                        _class="input-field"),
                    _class="collection-item"),
                LI(
                    DIV(
                        INPUT(_id="aa2", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota AA2", _for="aa2"),
                        _class="input-field"),
                    _class="collection-item"),
                LI(
                    DIV(
                        INPUT(_id="aa3", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota AA3", _for="aa3"),
                        _class="input-field"),
                    _class="collection-item"),
                LI(
                    DIV(
                        INPUT(_id="aa4", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota AA4", _for="aa4"),
                        _class="input-field"),
                    _class="collection-item"),

                LI("Nota da PAS", _class="collection-header"),
                LI(
                    DIV(
                        INPUT(_id="pas", _type="tel", _autocomplete="off", _class="peso_nao validate eh_nota"),
                        LABEL("Nota da PAS", _for="pas"),
                        _class="input-field"),
                    _class="collection-item"),

                _class="collection with-header"),
            DIV(A("Calcular", _class="waves-effect waves-light btn", _id="botao_calcular"), _style='text-align:center; margin-bottom: 10px;'),

            DIV( 
                A(
                    I(_class="fa fa-plus"),
                    _class="btn-floating btn-large orange"),
                UL(
                    LI(
                        A(
                            I(_class="fa fa-eraser"),
                            _class="btn-floating red", _id='botao_limpar'),
                        )
                    ),
                _class="fixed-action-btn horizontal"),
              DIV(
                DIV(
                  H4("Erro na nota"),
                  P("A nota deve ser um número de 0 à 10"),
                    _class="modal-content"),
                DIV(
                    A("OK", href="#!", _class="modal-action modal-close waves-effect waves-green btn-flat"),
                    _class="modal-footer"),
                _id="modalnotaerrada", _class="modal bottom-sheet"),
              DIV(
                DIV(
                  H4("Erro na nota"),
                  P("Há notas necessárias que estão vazias ou apresentam algum erro, não será possível calcular a nota!"),
                    _class="modal-content"),
                DIV(
                    A("OK", href="#!", _class="modal-action modal-close waves-effect waves-green btn-flat"),
                    _class="modal-footer"),
                _id="modalnotavazia", _class="modal bottom-sheet"),
              DIV(
                DIV(
                  H4("Erro nos pesos"),
                  P("Só é permitido adicionar pesos com valores de 0 à 10! Restaurando valores antigos!"),
                    _class="modal-content"),
                DIV(
                    A("OK", href="#!", _class="modal-action modal-close waves-effect waves-green btn-flat"),
                    _class="modal-footer"),
                _id="modalpesoerro", _class="modal bottom-sheet"),
        )
    footer=CAT(
                DIV(
                    DIV(
                        DIV(
                            DIV(_class="letras_conex", _id="letra01"),
                            DIV(_class="letras_conex", _id="letra02"),
                            DIV(_class="letras_conex", _id="letra03"),
                            DIV(_class="letras_conex", _id="letra04"),
                            DIV(_class="letras_conex", _id="letra05"),
                            DIV(_class="letras_conex", _id="letra06"),
                            DIV(_class="letras_conex", _id="letra07"),
                            DIV(_class="letras_conex", _id="didata"),
                            _id="logo_conex"),
                        _class='caixa_logo_principal'),
                    _class="conteiner"),
                DIV(

                    DIV(
                        "Conexão Didata ", XML("&copy;"), " 2011-",request.now.year,", Desenvolvido por PhanterJR",
                        _class='conteiner copyfooter'),
                    _class="footer-copyright")
                )
    
    return dict(header=header, main=main, footer=footer)

def sobre():
    hifen_attr={'_data-activates':"slide-out"}
    header=CAT(
                TAG['nav'](
                    DIV(
                        A("MINHA NOTA UNIT", _href=URL('www','index'), _class="brand-logo left minhanotaunit"),
                        _class="minhanotaunit nav_wrapper")
                    ),
                )

    main=DIV(
            UL(
                LI(H5("Objetivo"), _class="collection-header"),
                LI(
                    "O aplicativo tem como objetivo ajudar no cálculo da nota de cada disciplina dos cursos da UNIT",
                    _class="collection-item"),
                LI(H5("Versão"), _class="collection-header"),
                LI(
                    "1.0.0",
                    _class="collection-item"),
                LI(H5("Tecnologias Utilizadas"), _class="collection-header"),
                LI(
                    "Python",
                    _class="collection-item"),
                LI(
                    "Web2py",
                    _class="collection-item"),
                LI(
                    "Apache Cordova",
                    _class="collection-item"),
                LI(
                    "PhanterMobile Constructor",
                    _class="collection-item"),
                LI(
                    "HTML5",
                    _class="collection-item"),
                LI(
                    "CSS3",
                    _class="collection-item"),
                LI(
                    "Javascript",
                    _class="collection-item"),
                LI(
                    "Materializecss",
                    _class="collection-item"),
                LI(H5("Desenvolvimento"), _class="collection-header"),
                LI(
                    "Desenvolvido por PhanterJR, distribuído pela Conexão Didata sob a licença MIT.",
                    _class="collection-item"),

                _class="collection with-header"),

            DIV( 
                A(
                    I(_class="fa fa-reply"),
                    _href=URL('www', 'index'),
                    _class="btn-floating btn-large orange"),
                _class="fixed-action-btn horizontal"),
        )
    footer=CAT(
                DIV(
                    DIV(
                        DIV(
                            DIV(_class="letras_conex", _id="letra01"),
                            DIV(_class="letras_conex", _id="letra02"),
                            DIV(_class="letras_conex", _id="letra03"),
                            DIV(_class="letras_conex", _id="letra04"),
                            DIV(_class="letras_conex", _id="letra05"),
                            DIV(_class="letras_conex", _id="letra06"),
                            DIV(_class="letras_conex", _id="letra07"),
                            DIV(_class="letras_conex", _id="didata"),
                            _id="logo_conex"),
                        _class='caixa_logo_principal'),
                    _class="conteiner"),
                DIV(

                    DIV(
                        "Conexão Didata ", XML("&copy;"), " 2011-",request.now.year,", Desenvolvido por PhanterJR",
                        _class='conteiner copyfooter'),
                    _class="footer-copyright")
                )
    
    return dict(header=header, main=main, footer=footer)
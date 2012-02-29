# -*- coding: utf-8 -*-

from olympo.model.const_olympo import cl_Clases, clas_fechadecreacion, \
    clas_fechadeactualizacion, cl_Atributos, atri_fechadecreacion, \
    atri_fechadeactualizacion, clas_usuario, cl_Usuarios, atri_usuario, \
    usua_fechadecreacion, usua_fechadeactualizacion, usua_usuario, clas_nombre, \
    clas_descripcion, atri_nombre, atri_descripcion, atri_tamano, atri_clase, \
    atri_clasedeatributoenlazado, cl_Documentos, docu_fechadecreacion, \
    docu_fechadeactualizacion, docu_usuario, docu_autor, docu_formato, docu_tipo, \
    cl_FormatosDeDocumento, cl_TiposDeDocumento, fdd_fechadecreacion, \
    fdd_fechadeactualizacion, fdd_usuario, cl_UsuariosWeb, uswe_fechadecreacion, \
    uswe_fechadeactualizacion, uswe_usuario, cl_RepositoriosDeDocumentos, \
    cl_TiposDeValor, cl_TiposDeAtributo, atri_tipodevalor, atri_tipodeatributo, \
    tdv_fechadecreacion, tdv_fechadeactualizacion, tdv_usuario, tdv_nombre, \
    tdv_descripcion, tda_nombre, tda_descripcion, tda_fechadecreacion, \
    tda_fechadeactualizacion, tda_usuario, usua_nombre, docu_titulo, docu_notas, \
    usua_administrador, docu_privado
from olympo.util.util import nombre_tabla, cod_objeto, fecha_de_creacion, \
    fecha_de_actualizacion, atributo_objeto, valor_logico
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy.schema import Column
from sqlalchemy.types import Unicode, Text, Integer
    
DeclarativeBase = declarative_base()

class Clases(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_Clases)
    
    id_ = cod_objeto(cl_Clases)
    fecha_de_creacion_ = fecha_de_creacion(clas_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(clas_fechadeactualizacion)
    
    nombre = Column(clas_nombre, Unicode)
    descripcion = Column(clas_descripcion, Text)
    
    id_usuario = atributo_objeto(clas_usuario, cl_Usuarios)
    
class Atributos(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_Atributos)
    
    id_ = cod_objeto(cl_Atributos)
    fecha_de_creacion_ = fecha_de_creacion(atri_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(atri_fechadeactualizacion)
    
    nombre = Column(atri_nombre, Unicode)
    descripcion = Column(atri_descripcion, Text)
    tamano = Column(atri_tamano, Integer)
    
    id_usuario = atributo_objeto(atri_usuario, cl_Usuarios)
    
    id_clase = atributo_objeto(atri_clase, cl_Clases)
    id_clase_enlazada = atributo_objeto(atri_clasedeatributoenlazado, cl_Clases)
    id_tipo_de_valor = atributo_objeto(atri_tipodevalor, cl_TiposDeValor)
    id_tipo_de_atributo = atributo_objeto(atri_tipodeatributo, cl_TiposDeAtributo)
    
Clases.atributos = relation('Atributos', backref='clase',
                            primaryjoin=Clases.id_ == Atributos.id_clase)

Clases.atributos_enlazados = relation('Atributos', backref='clase_enlazada',
                                      primaryjoin=Clases.id_ == Atributos.id_clase_enlazada)

class TiposDeValor(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_TiposDeValor)
    
    id_ = cod_objeto(cl_TiposDeValor)
    fecha_de_creacion_ = fecha_de_creacion(tdv_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(tdv_fechadeactualizacion)
    
    nombre = Column(tdv_nombre, Unicode)
    descripcion = Column(tdv_descripcion, Text)
    
    id_usuario = atributo_objeto(tdv_usuario, cl_Usuarios)
    
    atributos = relation('Atributos', backref='tipo_de_valor')
    
class TiposDeAtributo(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_TiposDeAtributo)
    
    id_ = cod_objeto(cl_TiposDeAtributo)
    fecha_de_creacion_ = fecha_de_creacion(tda_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(tda_fechadeactualizacion)
    
    nombre = Column(tda_nombre, Unicode)
    descripcion = Column(tda_descripcion, Text)
    
    id_usuario = atributo_objeto(tda_usuario, cl_Usuarios)

class Usuarios(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_Usuarios)
    
    id_ = cod_objeto(cl_Usuarios)
    fecha_de_creacion_ = fecha_de_creacion(usua_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(usua_fechadeactualizacion)
    
    nombre = Column(usua_nombre, Unicode)
    administrador = valor_logico(usua_administrador)
    
    id_usuario = atributo_objeto(usua_usuario, cl_Usuarios)
    
class Documentos(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_Documentos)
    
    id_ = cod_objeto(cl_Documentos)
    fecha_de_creacion_ = fecha_de_creacion(docu_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(docu_fechadeactualizacion)
    
    titulo = Column(docu_titulo, Unicode)
    notas = Column(docu_notas, Text)
    privado = valor_logico(docu_privado)
    
    id_autor = atributo_objeto(docu_autor, cl_Usuarios)
    id_formato = atributo_objeto(docu_formato, cl_FormatosDeDocumento)
    id_tipo = atributo_objeto(docu_tipo, cl_TiposDeDocumento)
    
    id_usuario = atributo_objeto(docu_usuario, cl_Usuarios)
    
class FormatosDeDocumentos(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_FormatosDeDocumento)
    
    id_ = cod_objeto(cl_FormatosDeDocumento)
    fecha_de_creacion_ = fecha_de_creacion(fdd_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(fdd_fechadeactualizacion)
    
    id_usuario = atributo_objeto(fdd_usuario, cl_Usuarios)
    
class TiposDeDocumento(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_TiposDeDocumento)
    
    id_ = cod_objeto(cl_TiposDeDocumento)
    
class RepositoriosDeDocumentos(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_RepositoriosDeDocumentos)
    
    id_ = cod_objeto(cl_RepositoriosDeDocumentos)
    
class UsuariosWeb(DeclarativeBase):
    
    __tablename__ = nombre_tabla(cl_UsuariosWeb)
    
    id_ = cod_objeto(cl_UsuariosWeb)
    fecha_de_creacion_ = fecha_de_creacion(uswe_fechadecreacion)
    fecha_de_actualizacion_ = fecha_de_actualizacion(uswe_fechadeactualizacion)
    
    id_usuario = atributo_objeto(uswe_usuario, cl_Usuarios)
    
create database if not exists prueba;
use prueba;

create table usuarios(
    id int auto_increment not null,
    nombre text,
    apellidos text,
    email text not null,
    contrasena text not null,
    fecha date not null,
    constraint pk_usuarios primary key(id),
    constraint uq_email unique(email)
)ENGINE=InnoDb;

create table notas(
    id int auto_increment not null,
    usuario_id int not null,
    titulo text not null,
    descripcion text,
    fecha date not null,
    constraint pk_notas primary key(id),
    constraint fk_nota_usuario foreign key(usuario_id) references usuarios(id)
)ENGINE=InnoDb;
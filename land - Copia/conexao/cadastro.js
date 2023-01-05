const db = require('./db')

const cadastro = db.sequelize.define('cadastros', {
    nome: {
        type: db.Sequelize.STRING
    },
    sobrenome: {
        type: db.Sequelize.STRING
    },
    cpf: {
        type: db.Sequelize.STRING
    },
    email: {
        type: db.Sequelize.STRING
    },
    telefone: {
        type: db.Sequelize.STRING
    },
    
})

//cadastro.sync({ force: true })

module.exports = cadastro;

const cadastro2 = db.sequelize.define('cadastros', {
    empresa: {
        type: db.Sequelize.STRING
    },
    cnpj: {
        type: db.Sequelize.STRING
    },
    razao_social: {
        type: db.Sequelize.STRING
    },
    email: {
        type: db.Sequelize.STRING
    },
    telefone: {
        type: db.Sequelize.STRING
    },
})

//cadastro2.sync({ force: true })

module.exports = cadastro2;
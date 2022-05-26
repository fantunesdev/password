# Sistema para gerar senhas randômicas

## Considere a seguinte necessidade:
 
Precisamos enviar uma senha de maneira segura para um cliente. Para isso, ao invés de encaminhá-la via E-mail, SMS, Slack, etc, foi dado como solução o desenvolvimento de um sistema com as seguintes funções:
 
1- Sistema gera <strong>senha aleatória</strong> baseada em <strong>políticas de complexidade</strong> (tipo de caracteres, números, letras, tamanho, etc); 
- **Exemplo**: o usuário ao clicar no botão "Gerar Senha" irá obter uma senha aleatória;

2- Usuário irá especificar <strong>quantas vezes</strong> a senha gerada poderá ser vista e <strong>qual o tempo</strong> que a senha ficará válida;
- **Exemplo**: o usuário irá especificar que a senha possa ser vista apenas <em>duas vezes</em> pelo prazo de <em>um dia</em>;

3- O sistema irá <strong>gerar uma URL</strong> que dá acesso a visualização da senha, baseando-se nos critérios do item 02;
- **Exemplo**: o usuário enviará a URL para que o cliente possa visualizar a senha;

4- Após atingir a quantidade de visualizações ou o tempo disponível, o sistema <strong>bloqueia/elimina</strong> a visualização da senha (expirado).
A senha <strong>não deve ser armazenada</strong> após sua expiração

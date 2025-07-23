
# Não esta em uso, mas aqui tem umas explicações legais sobre as permições não prontas 

from rest_framework import permissions

# Não esta em uso
class GenrePermissionClass(permissions.BasePermission):
    # Não esta em uso
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            # 'genres.views_genre' é um padrão: 1.Nome da app; 2.Nome da ação(ex: delete, view); 3.Nome do model
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False
    
# Não esta em uso
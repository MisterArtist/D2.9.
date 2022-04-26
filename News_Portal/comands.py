u1 = User.objects.create_user(username='Evgeniy')
u2 = User.objects.create_user(username='Yuriy')

Author.objects.create(autorUser=u1)
Author.objects.create(autorUser=u2)

Category.objects.create(name='IT')
Category.objects.create(name='WORLD')
Category.objects.create(name='AUTO')
Category.objects.create(name='MUSIC')

Post.objects.create(author=author, categoriType='NW', title='sometitle', text='somebigtext')

Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))

Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextbyauthor')

Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).rating

Author.objects.get(id=1)
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor

Post.objects.get(id=1).like()
a.update_rating()
a.ratingAuthor

a = Author.objects.order_by('-ratingAuthor')
a
a = Author.objects.order_by('-ratingAuthor')[:1]

for i in a:
    i.ratingAuthor
    i.authorUser.username

# Maintainer: IGN-STYLY on github.com <suporte.lazar@gmail.com>
pkgname=Lotus
pkgver=0.1
pkgrel=1
pkgdesc="BETA"
arch=(x86_64)
url="https://github.com/IGN-Styly/Lotus"
license=('MIT')
depends=()
makedepends=()
checkdepends=()
provides=(lotus)
source=("git+$url")
install=
md5sums('SKIP')
noextract=()

prepare() {
	cd "$pkgname-$pkgver"
	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
}

build() {
	cd "$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

check() {
	cd "$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}

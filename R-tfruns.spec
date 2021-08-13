#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tfruns
Version  : 1.5.0
Release  : 26
URL      : https://cran.r-project.org/src/contrib/tfruns_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tfruns_1.5.0.tar.gz
Summary  : Training Run Tools for 'TensorFlow'
Group    : Development/Tools
License  : Apache-2.0
Requires: R-base64enc
Requires: R-config
Requires: R-jsonlite
Requires: R-magrittr
Requires: R-reticulate
Requires: R-rlang
Requires: R-rstudioapi
Requires: R-tidyselect
Requires: R-whisker
Requires: R-yaml
BuildRequires : R-base64enc
BuildRequires : R-config
BuildRequires : R-jsonlite
BuildRequires : R-magrittr
BuildRequires : R-reticulate
BuildRequires : R-rlang
BuildRequires : R-rstudioapi
BuildRequires : R-tidyselect
BuildRequires : R-whisker
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
training run. Provides a unique, time stamped directory for each run
  along with functions to retrieve the directory of the latest run or 
  latest several runs.

%prep
%setup -q -c -n tfruns
cd %{_builddir}/tfruns

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614361583

%install
export SOURCE_DATE_EPOCH=1614361583
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tfruns
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tfruns
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tfruns
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tfruns || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tfruns/DESCRIPTION
/usr/lib64/R/library/tfruns/INDEX
/usr/lib64/R/library/tfruns/Meta/Rd.rds
/usr/lib64/R/library/tfruns/Meta/features.rds
/usr/lib64/R/library/tfruns/Meta/hsearch.rds
/usr/lib64/R/library/tfruns/Meta/links.rds
/usr/lib64/R/library/tfruns/Meta/nsInfo.rds
/usr/lib64/R/library/tfruns/Meta/package.rds
/usr/lib64/R/library/tfruns/Meta/vignette.rds
/usr/lib64/R/library/tfruns/NAMESPACE
/usr/lib64/R/library/tfruns/NEWS.md
/usr/lib64/R/library/tfruns/R/tfruns
/usr/lib64/R/library/tfruns/R/tfruns.rdb
/usr/lib64/R/library/tfruns/R/tfruns.rdx
/usr/lib64/R/library/tfruns/doc/index.html
/usr/lib64/R/library/tfruns/doc/managing.R
/usr/lib64/R/library/tfruns/doc/managing.Rmd
/usr/lib64/R/library/tfruns/doc/managing.html
/usr/lib64/R/library/tfruns/doc/overview.R
/usr/lib64/R/library/tfruns/doc/overview.Rmd
/usr/lib64/R/library/tfruns/doc/overview.html
/usr/lib64/R/library/tfruns/doc/tuning.R
/usr/lib64/R/library/tfruns/doc/tuning.Rmd
/usr/lib64/R/library/tfruns/doc/tuning.html
/usr/lib64/R/library/tfruns/help/AnIndex
/usr/lib64/R/library/tfruns/help/aliases.rds
/usr/lib64/R/library/tfruns/help/paths.rds
/usr/lib64/R/library/tfruns/help/tfruns.rdb
/usr/lib64/R/library/tfruns/help/tfruns.rdx
/usr/lib64/R/library/tfruns/html/00Index.html
/usr/lib64/R/library/tfruns/html/R.css
/usr/lib64/R/library/tfruns/rstudio/addins.dcf
/usr/lib64/R/library/tfruns/tests/testthat.R
/usr/lib64/R/library/tfruns/tests/testthat/extra.dat
/usr/lib64/R/library/tfruns/tests/testthat/flags-learning-rate.yml
/usr/lib64/R/library/tfruns/tests/testthat/flags-override.yml
/usr/lib64/R/library/tfruns/tests/testthat/flags-precision.R
/usr/lib64/R/library/tfruns/tests/testthat/flags-profile-override.yml
/usr/lib64/R/library/tfruns/tests/testthat/flags.rds
/usr/lib64/R/library/tfruns/tests/testthat/helper.R
/usr/lib64/R/library/tfruns/tests/testthat/metrics.rds
/usr/lib64/R/library/tfruns/tests/testthat/subdir/extra.dat
/usr/lib64/R/library/tfruns/tests/testthat/test-copy.R
/usr/lib64/R/library/tfruns/tests/testthat/test-flags.R
/usr/lib64/R/library/tfruns/tests/testthat/test-run-data.R
/usr/lib64/R/library/tfruns/tests/testthat/test-runs.R
/usr/lib64/R/library/tfruns/tests/testthat/test-tuning.R
/usr/lib64/R/library/tfruns/tests/testthat/train-error.R
/usr/lib64/R/library/tfruns/tests/testthat/train.R
/usr/lib64/R/library/tfruns/tests/testthat/write_run_data.R
/usr/lib64/R/library/tfruns/views/compare_runs.html
/usr/lib64/R/library/tfruns/views/components/c3.html
/usr/lib64/R/library/tfruns/views/components/dashboard.html
/usr/lib64/R/library/tfruns/views/components/diff2html.html
/usr/lib64/R/library/tfruns/views/components/highlight_js.html
/usr/lib64/R/library/tfruns/views/components/jquery-AUTHORS.txt
/usr/lib64/R/library/tfruns/views/components/jquery.html
/usr/lib64/R/library/tfruns/views/components/material_icons.html
/usr/lib64/R/library/tfruns/views/components/materialize.html
/usr/lib64/R/library/tfruns/views/components/metrics_charts.html
/usr/lib64/R/library/tfruns/views/components/roboto.html
/usr/lib64/R/library/tfruns/views/components/vue_js.html
/usr/lib64/R/library/tfruns/views/components/vue_min_js.html
/usr/lib64/R/library/tfruns/views/metrics.html
/usr/lib64/R/library/tfruns/views/view_run.html

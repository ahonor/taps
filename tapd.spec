name: tapd
version: 1.0.1
release: 1
summary: Tap Service Daemon 
group: rundeck
license: GPL
url: http://github.com/dtolabs/taps

requires: lighttpd >= 1.4
requires(post): chkconfig
requires(postun): chkconfig

%description
Rundeck supports dynamic input fields using valueUrls.  These urls can be served from the file system using file:// or http:// using a webservice.  This webservice provides a mechanism to serve dynamic options in an easy to use, easy to integration fashion.

The webservice uses the CGI standard to return json to Rundeck.  By placing a file with the *.options under the /var/rundeck directory, any acceptable #! can be used to process the CGI request.

%files
%defattr(644, tapd, tapd, 755)
%config(noreplace) %attr(-, tapd, tapd) /etc/tapd/options.conf
%attr(755, -, -) /etc/rc.d/init.d/tapd
%attr(-, tapd, tapd) %dir   /var/log/tapd
%attr(-, tapd, tapd) %ghost /var/log/tapd/error.log
%attr(-, tapd, tapd) %ghost /var/log/tapd/access.log
%attr(-, tapd, tapd) %ghost /var/log/tapd/dav.access.log
%attr(-, tapd, tapd) %dir   /var/tapd/dav
%attr(755, -, -) /usr/sbin/tapd

%pre
getent group  tapd >/dev/null || groupadd tapd
getent passwd tapd >/dev/null || useradd -m -g tapd tapd

%post
/sbin/chkconfig --add tapd

%postun
if [ "$1" = 0 ]; then
	/sbin/chkconfig --del tapd
fi

%changelog
* Thu Jun 06 2013 Alex Honor <alexhonor@gmail.com> 1.1.1
	- Changed package group, and document-root.	
* Wed Oct 20 2010 Noah Campbell <noahcampbell@gmail.com> 1.0
	- Initial spec file.	

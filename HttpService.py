#implement the services functionality

class HttpService : public QtService<QCoreApplication>
 {
 public:
     HttpService(int argc, char **argv)
         : QtService<QCoreApplication>(argc, argv, "Qt HTTP Daemon")
     {
         setServiceDescription("A dummy HTTP service implemented with Qt");
         setServiceFlags(QtServiceBase::CanBeSuspended);
     }

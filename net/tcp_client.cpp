#include <winsock2.h>
#include <stdio.h>
#include <Ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
void main()
{
	//��ʼ���׽���
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2,2);
	WSAStartup(wVersionRequested, &wsaData);

	//�����׽���
	SOCKET sockClient = socket(AF_INET, SOCK_STREAM, 0);
	//Socket��ַ�ṹ��Ĵ���
	SOCKADDR_IN addrSrv;

	struct in_addr addr;
	inet_pton(AF_INET, "127.0.0.1", (void*)&addr);
	addrSrv.sin_addr.S_un.S_addr = addr.s_addr;
	addrSrv.sin_family = AF_INET;//ָ����ַ��
	addrSrv.sin_port = htons(6000);


	connect(sockClient, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));

	char recvBuf[100] = { 0 };//��ʼ��Ϊ0�������淢�͵�ʱ��strlen �Ͳ���Ҫ��1
	char sendBuf[100] = { 0 };
	while (1)
	{
		//���ԭ������
		memset(recvBuf, 0, sizeof(recvBuf));
		recv(sockClient, recvBuf, 100, 0);

		printf("%s\n", recvBuf);

		//���ԭ������
		memset(sendBuf, 0, sizeof(sendBuf));
		gets_s(sendBuf);

		send(sockClient, sendBuf, strlen(sendBuf), 0);

	}
	//�ر��׽��֡�
	closesocket(sockClient);
	printf("client close\n");
	WSACleanup();//���������������������
}